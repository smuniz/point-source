/* A very simple function to test a do while() loop. */

int test54(int var1) {
	int n = 0;
	do {
		if (var1 > 10) {
			var1 = 20;
		};
		n++;
		var1--;
	} while (n < 10);
	return var1;
}

