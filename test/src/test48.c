/* A simple function to test an if statement with multiple expressions. */

int test48(int value1, int value2, int value3 );

int test48(int value1, int value2, int value3 ) {
	int local1 = 0;
//	if ((value1 == 1) && (value2 == 2) || (value3 != 3)) {
	if (value1 == 1) {
		if (value2 == 2) {
			step4:
			local1 = 10;
			value3 = 10;
			goto exit;
		} else {
			step5:
			local1 = 20;
			value3 = 20;
			goto exit;
		}
	} else {
		if (value3 == 3) {
			goto step5;
		} else {
			goto step4;
		}
	}
exit:
	return local1;
}

