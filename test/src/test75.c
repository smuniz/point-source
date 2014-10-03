/* A very simple function to test casting signed i32 to i64. */
#include <stdint.h>

int64_t test75 ();

int64_t test75 ( ) {
	int32_t rel32;
	int64_t rel64;
	rel32 = 0x1000;
	rel64 = rel32;
	return rel64;
}

