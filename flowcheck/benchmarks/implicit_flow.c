// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char ** argv) {
	int h = *argv[1];
	FC_TAINT_WORD(&h);
    int l = 0;
		if (h == 1) {
			l = 1;
		}
		if (h == 1) {
			l = 1;
		}
		if (h == 2) {
			l = 2;
		}
		if (h == 3) {
			l = 3;
		}
		if (h == 4) {
			l = 4;
		}
		if (h == 5) {
			l = 5;
		}
		if (h == 6) {
			l = 6;
		}
		if (h == 7) {
			l = 0;
		}
		printf("%d\n", l);
        return l;
}