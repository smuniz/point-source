/* Tests the translation of the ADD, IF COND 4(Equal) instruction pair. */
/* gcc seems to compile with an unneeded repz. repz not yet handled by libbeauty.
   So for this test, compile with clang. */
/* clang -c -O2 -o test71.o test71.c */

int test71(int var1, int var2, int var3, int var4, int var5)
{
	int tmp;
	tmp = var1 & var2;
	if (var1 + var2 != 0) {
		var3 = var3 + var4 + tmp;
	}
	return var3;
}	

