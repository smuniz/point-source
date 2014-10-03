/* A very simple function to test one call param that passes the value of a parameter. */

int test20b(int value2 );

int test20b(int value2 )
{
	return value2 + 10;
}

int test20a(int value1)
{
	return test20b(value1);
}

