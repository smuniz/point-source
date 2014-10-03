/* A very simple function to test a do while() loop contained in a if...then...else. */

int test57(int var1) {
	int n;
	if (var1 == 1) {
		do {
			n++;
			var1--;
		} while (n < 10);
	}
	return var1;
}

