/* A very simple function to test a nested for loop. */

int test52(int param1, int param2);

int test52(int param1, int param2) {
	int n, m;
	if (param1 == 2) {
		param2++;
	}
	for (n = 0; n < 10; n++) {
		param2+=10;
		if (n == 5) {
			param1+=2;
		}
		for (m = 0; m < 5; m++) {
			param1+=5;
		}
		for (m = 0; m < 4; m++) {
			param1+=4;
		}
	}
	return param1 + param2;
}

