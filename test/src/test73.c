/* A very simple function to test two functions. */

int test73a(int value1 ) {
	int local1 = value1;
	if (value1 > 5) {
		local1 = value1 + 10;
		return local1;
	}
	return 1;
}

int test73b(int value1 ) {
	int local1 = value1;
	if (value1 > 6) {
		local1 = value1 + 12;
		return local1;
	}
	return 12;
}

