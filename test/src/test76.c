/* A very simple function to test casting unsigned i32 to i64. */
#include <stdint.h>

uint64_t test76 ();

uint64_t test76 ( ) {
	uint32_t rel32;
	uint64_t rel64;
	rel32 = 0x1000;
	rel64 = rel32;
	return rel64;
}

