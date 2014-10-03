/* A very simple function to test memory stores. */

#include <stdint.h>

int32_t mem1;

int test81() {
	int32_t *ptr1;
	uint8_t *ptr2;
	ptr1 = &mem1;
	ptr2 = (uint8_t *)ptr1;
	*ptr1 = 0x2021;
	*ptr2 = 0x12;
	return 0;
}

