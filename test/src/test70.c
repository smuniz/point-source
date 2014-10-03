/* Tests the translation of the AND, IF instruction pair. */
/* gcc seems to compile with an unneeded repz. repz not yet handled by libbeauty.
   So for this test, compile with clang. */
/* clang -c -O2 -o test70.o test70.c */

int test70(int var1, int var2, int var3, int var4, int var5)
{
	int tmp;
	tmp = var1 & var2;
	if (var1 & var2) {
		var3 = var3 + var4 + tmp;
	} else {
		var3 = var3 + var5;
	}
	return var3;
}	

