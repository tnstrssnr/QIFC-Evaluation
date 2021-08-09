// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char ** argv) {
	int h = *argv[1];
	FC_TAINT_WORD(&h);

    int l;
    if (0 <= h && h < 16) {
		l = h + 3;
	} else {
		l = 3;
	}
	printf("%d\n", l);
    return l;
}