// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char **argv) {
		int h = *argv[1];
		FC_TAINT_WORD(&h);

		int l = mask0123(h);
		printf("%d\n", l);
		return 0;
	}

int mask0(int h) {
		return h | (1 << 0);
	}
int mask1(int h) {
		return h | (1 << 1);
	}

int mask2(int h) {
		return h | (1 << 2);
	}

int mask3(int h) {
		return h | (1 << 3);
	}

int mask01(int h) {
		return mask1(mask0(h));
	}

int mask012(int h) {
		return mask2(mask01(h));
	}

int mask0123(int h) {
		return mask3(mask012(h));
	}