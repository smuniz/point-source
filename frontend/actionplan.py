# 
# Copyright (c) 2017 Sebastian Muniz
# 
# This code is part of point source decompiler
#

from traceback import format_exc


class Action(object):
    """..."""

    def __ini__(self, _type=None):
        pass

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, address):
        self.address = address

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, _type):
        self._type = _type


class ActionPlanException(Exception):
    """..."""
    pass


class ActionPlan(object):
    """..."""

    def __init__(self):
        self.actions = list()

    @staticmethod
    def new_action(self):
        """Return a new action instance already appended to the actions
        list.
        
        """
        #
        # Create a new plan instance and store it before returning it.
        #
        new_action = ActionPlan()
        self.actions.append(new_action)
        return new_action

    def has_plan_for_address(self, address):
        """Return whether or not the specified address as an associated
        plan.
        
        """
        return address in [action.address for action in self.actions]
