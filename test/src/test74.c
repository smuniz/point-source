/* A very simple function to test casting i64 to i32. */
#include <stdint.h>

int32_t test74 ();

int32_t test74 ( ) {
	int32_t rel32;
	int64_t rel64;
	rel64 = 0x1000;
	rel32 = rel64;
	return rel32;
}

