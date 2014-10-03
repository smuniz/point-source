/* A very simple function to test a "call" after an "if" statement */

int test25b(int value2 );

int test25b(int value2 )
{
	return value2 + 10;
}

int test25a(int value1)
{
	if (value1 > 10) {
		return test25b(value1);
	}
	return 0;
}

