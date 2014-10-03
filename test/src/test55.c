/* A simple function to test an if statement with multiple expressions. */

int test55(int value1, int value2, int value3 );

int test55(int value1, int value2, int value3 ) {
	int local1 = 0;
	if (((value1 == 1) && (value2 == 1)) || ((value1 != 1) && (value3 == 1))) {
		local1 = 10;
	} else {
		local1 = 1;
	}
	return local1;
}

