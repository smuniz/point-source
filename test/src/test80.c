/* A very simple function to test memory stores. */

int test80(char *value1 ) {
	int local;
	value1 = value1 + 10;
	local = *value1;	
	return local;
}

