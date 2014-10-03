/* A very simple function to test a nested for loop. */

int test51();

int test51() {
	int local1, local2, n, m;
	for (n = 0; n < 10; n++) {
		local2+=10;
		if (n == 5) {
			local1+=2;
			break;
		}
	}
	return local1 + local2;
}

