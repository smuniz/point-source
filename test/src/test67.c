/* A very simple TEST instruction. */

int test67(int value1 ) {
	int local1 = 1;
	if (value1 & 5) {
		local1 = value1 + 10;
	}
	return local1;
}

