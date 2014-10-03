/* A very simple function to test memory stores. */

static int mem1[2] = {0x123,0x100};

int test79(int value1 );

int test79(int value1 ) {
	int local;
	local = value1 + mem1[1];	
	return local;
}

