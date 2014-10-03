/* A very simple function to test a nested for loop. */

int test59(int param1, int param2);

int test59(int param1, int param2) {
	int n, m;
	do {
		if (param2 == 5) {
			param1 = 1;
			break;
		}
	} while( param2 != 0);
	return param1 + param2;
}

