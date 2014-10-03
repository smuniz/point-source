/* A very simple function to test a do while() loop. */

int test47(int var1) {
	int n = 0;
	do {
		n++;
		var1--;
		if (var1 > 10) {
			var1 = 20;
		};
	} while (n < 10);
	return var1;
}

