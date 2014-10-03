/* Test multi-entry loop */

int test60 ( int value );

int test60 ( int value ) {
  if (value == 1) {
    goto two;
  }
  
  while (value == 2) {
    value += 2;
    two:
    value++;
  }
  return value;
}

