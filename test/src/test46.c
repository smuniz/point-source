/* A very simple function to test a loop with an if in it. */

int test46();

int test46() {
	int local1, local2, n, m;
	for (n = 0; n < 10; n++) {
		local2+=10;
		if (local2 > 20) {
			local1+=5;
		}
	}
	return local1 + local2;
}

