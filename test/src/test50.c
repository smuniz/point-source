/* A very simple function to test CMOV. */

int test50(int value1 );

int test50(int value1 ) {
	int local1 = 0;
	if (value1 > 5) {
		local1 = 10;
	}
	return local1;
}

