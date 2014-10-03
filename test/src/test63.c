/* A very simple jump table. */

int test63(int var1, int var2) {
	int n = 0;
	switch (var1) {
	case 1:
		n = var2 + 1;
		break;
	case 2:
		n = 2;
		break;
	case 3:
		n = 3;
		break;
	case 4:
		n = 4;
		break;
	case 5:
		n = 5;
		break;
	}
	return n;
}

