/* A very simple function to test a nested for loop. */

int test53(int param1, int param2);

int test53(int param1, int param2) {
	int n, m;
	while( param2 != 0) {
		if (param2 == 5) {
			param2 = 0;
			continue;
		}
		param1 += param2;
	}
	return param1 + param2;
}

