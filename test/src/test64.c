/* A very simple function pointer. */

//int add_int2(int n, int m) {
//	return n + m;
//}
#include <inttypes.h>

typedef int (*my_func_def)(int, int);
/* note that the typedef name is indeed my_func_def */

int test63(my_func_def function_ptr) {
	int tmp;
	__uint128_t test;
	test = 100;
	tmp = function_ptr(1, 2);
	return test;
}

