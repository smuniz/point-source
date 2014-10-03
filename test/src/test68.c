/* A very simple function to test flag dual users.
I.e. Two branch instruction from the same CMP */

int test68(int var1, int var2, int var3, int var4, int var5)
{
	if (var1 >= var2) {
		if (var1 == var2) var3 = var3 + var4;
		else var3 = var3 + var5;
	}
	return var3;
}	

