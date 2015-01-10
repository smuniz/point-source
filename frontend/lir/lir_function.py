# 
# Copyright (c) 2014 Sebastian Muniz
# 
# This code is part of point source decompiler
#


class LowLevelFunctionException(Exception):
    """Generic exceptino for the low-level function IR."""
    pass


class LowLevelFunction(object):
    """This class holds all the information obtained from the different phases
    of the analysis and it includes instructions, basic blocks boundaries, etc.

    """

    def __init__(self, start_address, end_address, func_name, iset):
        """Instance initialization."""
        #Store information about the function being analyzed.
        self.start_address = start_address
        self.end_address = end_address
        self.name = func_name

        self.iset = iset

        self.basic_blocks = list()

        self.sp_regs = list()  # Registers list to access local variables
        self.stack_size = 0

        self.leaf_procedure = True

        # def-use and use-def chains definitions used for optimizations and
        # analysis.
        self.du_chain = dict()
        self.ud_chain = dict()

        # Epilogue and prologue instruction addresses inside the current
        # function.
        self.prologue_addresses = list()
        self.epilogue_addresses = list()

        # Non-volatile registers list.
        self.nv_regs = list()

        # Regsiters used as functions arguments.
        self.param_regs = dict()

        # Indicate wheather the function returns to its caller or not.
        self.ret_to_caller = False

        self.stack_restore = "Unknown"

        self.compiler_type = None #self.debugger.COMPILER_UNK

        # Create basic return types in order to create the function skeleton.
        # At the moment we just create generic (integer) types with the right
        # amount of return values.
        self.return_type = None
        self.return_registers = list()

    def add_prologue_address(self, address):
        """Mark the specified address as part of the function prologue and
        remove it from the list of statements to analyze.

        """
        self.prologue_addresses.append(address)

    def add_epilogue_address(self, address):
        """Mark the specified address as part of the function epilogue and
        remove it from the list of statements to analyze.

        """
        self.epilogue_addresses.append(address)

    @property
    def leaf_procedure(self):
        """Indicate whether the current function is a leaf procedure or not."""
        return self._leaf_procedure

    @leaf_procedure.setter
    def leaf_procedure(self, leaf_procedure=False):
        """Store the size of bytes of the function stack. """
        self._leaf_procedure = leaf_procedure

    @property
    def stack_size(self):
        """Return the size of bytes of the function stack."""
        return self._stack_size

    @stack_size.setter
    def stack_size(self, size):
        """Store the size of bytes of the function stack. """
        self._stack_size = size

    @property
    def start_address(self):
        """Return the start address of the function."""
        return self._start_address

    @start_address.setter
    def start_address(self, address):
        """Store the start address of the function."""
        self._start_address = address

    @property
    def end_address(self):
        """Return the end address of the function."""
        return self._end_address

    @end_address.setter
    def end_address(self, address):
        """Store the end address of the function."""
        self._end_address = address

    def has_address(self, address):
        """Return a boolean indicating if the specified address is contained
        inside the current function.

        """
        for basic_block in self:
            if basic_block.has_address(address):
                return True

        return False

    def add_basic_block(self, bblock):
        """Append the specified basic block to the current list."""
        self.basic_blocks.append(bblock)

        # Add a cross reference to ourselves.
        bblock.function = self

    def get_basic_block_index(self, bblock):
        """Return the position in the basic blocks list of the basic block
        specified to use as index.

        """
        return self.basic_blocks.index(bblock)

    def get_basic_block(self, index):
        """Return the basic block at the specified position in the basic blocks
        list.

        """
        return self.basic_blocks[index]

    def get_basic_block_by_address(self, ea):
        """Return the basic block whose address range accomodates the specified
        address.

        """
        for bblock in self:
            if bblock.has_address(ea):
                return bblock
        return None

    @property
    def name(self):
        """Return the name of the function."""
        return self._name

    @name.setter
    def name(self, name):
        """Store the name of the function."""
        self._name = name

    def __str__(self):
        """Return the function string representation."""
        function_repr = "# " + " S U B R O U T I N E ".center(70, "=")
        function_repr += "\n        .globl %s\n\n" % self.name

        #
        # Get all the basic blocks inside this function.
        #
        #function_repr += "\n".join([str(basic_block) for basic_block in self])
        for basic_block in self:
            for inst in basic_block:

                if inst.address in self.prologue_addresses:
                    attrib = "prolog"
                elif inst.address in self.epilogue_addresses:
                    attrib = "epilog"
                else:
                    attrib = "      "

                # Generate the final instruction reprenstation containing all
                # the information gathered.
                function_repr += \
                    "%08X %s %-30s\t; DU=%-20s\n\t\t\t\t\t; UD=%-20s\n" % (
                    inst.address,
                    attrib,
                    inst,
                    self.du_chains_printable(inst.address),
                    self.ud_chains_printable(inst.address)
                    )
            function_repr += "\n"

        function_repr += "\n# " + ("=" * 70)

        return function_repr

    def du_chains_printable(self, address):
        """Generate a printable string representation of the def-use chains for
        the current instruction.

        """
        du_chains_repr = "["
        if address in self.du_chain:
            for cur_def in self.du_chain[address]:
                if cur_def in self.du_chain[address]:

                    du_chains_repr += "{r%-2s : " % cur_def

                    for use in self.du_chain[address][cur_def]:
                        du_chains_repr += "0x%X " % use

                    du_chains_repr += "}"
        du_chains_repr += "]"
        return du_chains_repr

    def ud_chains_printable(self, address):
        """Generate a printable string representation of the use-def chains for
        the current instruction.

        """
        ud_chains_repr = "["
        if address in self.ud_chain:
            for cur_use in self.ud_chain[address]:
                if cur_use in self.ud_chain[address]:

                    ud_chains_repr += "{r%-2s : " % cur_use

                    _def = self.ud_chain[address][cur_use]

                    ud_chains_repr += "0x%X " % _def

                    ud_chains_repr += "}"
        ud_chains_repr += "]"
        return ud_chains_repr

    def __getitem__(self, key):
        """Return the basic block(s) matching the specified index(es)."""
        if isinstance(key, slice):
            indices = key.indices(len(self))
            return [self[i] for i in xrange(*indices)]
        elif isinstance(key, int) or isinstance(key, long):
            try:
                return self.get_basic_block(key)
            except KeyError:
                raise IndexError
        else:
            raise TypeError

    def __len__(self):
        """Return the count of basic blocks currently stored."""
        return len(self.basic_blocks)

    @property
    def instructions_count(self):
        """Get the total number of instructions in the current function."""
        count = 0
        for inst in self.basic_blocks:
            count += len(inst)
        return count

    def get_basic_blocks_count(self):
        """Get the total number of basic blocks in the current function."""
        return len(self)

    def add_stack_access_register(self, reg):
        if reg not in self.sp_regs:
            self.sp_regs.append(reg)

    @property
    def stack_access_registers(self):
        return self.sp_regs

    @property
    def instruction_set(self):
        """Return the instruction set for the current architecture."""
        return self._instruction_set

    @instruction_set.setter
    def instruction_set(self, i_set):
        """Store the instruction set to use with the current architecture."""
        self._instruction_set = i_set

    def generate_chains(self):
        """
        Generate def-use and use-def chains for the low level IR so further
        analysis can me performed, i.e. live analysis, dead code elimination,
        and other information gathering so that the MIR will be optimized.

        """
        reg_defs = dict()
        prev_reg_def = dict()

        for bb_index, lir_bb in enumerate(self):

            for lir_inst in lir_bb:

                self.du_chain.setdefault(lir_inst.address, dict())
                self.ud_chain.setdefault(lir_inst.address, dict())

                if self.iset.is_branch(lir_inst.type):
                    # TODO / FIXME : This is a kludge for PPC.
                    #
                    # Let's assume that when a call instruction is found all
                    # the temporal registers might have been modified inside
                    # the callee.
                    for reg,v in reg_defs.items():
                        #print "Reg %s at address 0x%08x" % (
                        #    self.iset.GPR_NAMES[reg],v)

                        if reg in self.iset.VOLATILE_REGISTERS:
                            # print "Removing volatile register %s before branch at 0x%X" % (
                            #     self.iset.GPR_NAMES[reg],
                            #     lir_inst.address)
                            del reg_defs[reg]

                else:
                    pass

                prev_reg_def.clear() # Only valid during the current
                                        # instruction being analyzed.

                for lir_op_idx, lir_op in enumerate(lir_inst.operands):

                    if not lir_op.is_reg:
                        # Only work on tempoerary registers.
                        continue

                    op = lir_op.value

                    if self.__is_destination_operand(lir_inst, lir_op_idx):
                        if op in reg_defs:
                            prev_reg_def[op] = reg_defs[op]
                        reg_defs[op] = lir_inst.address

                        defs = self.du_chain.get(lir_inst.address, None)

                        if defs is None:
                            raise Exception(
                                "Invalid DU chain detected for 0x%08X" % \
                                lir_inst.address)

                        defs.setdefault(op, list())

                    else:
                        # Make use of original definition in cases where the
                        # same register is both source and destination operand.
                        def_address = prev_reg_def.get(op, None)

                        if def_address is None:
                            def_address = reg_defs.get(op, None)

                        if def_address is not None:
                            cur_address = lir_inst.address

                            #
                            # Update def-use chain.
                            #
                            defs = \
                                self.du_chain.setdefault(def_address, dict())

                            cur_def = defs.setdefault(op, list())
                            cur_def.append(cur_address)

                            #
                            # Update use-def chain.
                            #
                            uses = self.ud_chain.get(cur_address, None)

                            if uses is None:
                                raise Exception(
                                    "Invalid UD chain detected for 0x%08X" % \
                                    cur_address)
                            uses[op] = def_address

    def __is_destination_operand(self, lir_inst, lir_op_idx):
        """Indicate if the specified operand is being treated
        as a destion operand (meaning its content is going to
        change).

        """
        # FIXME : Remove IDA-specific code.
        from idaapi import CF_CHG1, CF_CHG2, CF_CHG3, CF_CHG4, CF_CHG5, CF_CHG6 
        changes = {
            0 : CF_CHG1,
            1 : CF_CHG2,
            2 : CF_CHG3,
            3 : CF_CHG4,
            4 : CF_CHG5,
            5 : CF_CHG6,
        }
        return changes.get(lir_op_idx, None) in lir_inst.features
