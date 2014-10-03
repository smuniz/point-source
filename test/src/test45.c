/* A very simple function to test an if statement. */
/* with a simple forward goto. */

int test45(int value1 );

int test45(int value1 ) {
	int local1 = value1;
	if (value1 > 5) {
		local1 = value1 + 10;
		if (value1 > 10) {
			local1 = local1 + 11;
		}
	}
	return local1;
}

