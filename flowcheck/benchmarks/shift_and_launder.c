// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int hargc, char ** argv) {
	int h = *argv[1];
	FC_TAINT_WORD(&h);
    int launder = 0;
	int shift = 1;
	int i = 0;

	while (i != h1) {
		launder += 1;
		shift = shift << 1;
		i++;
	}
	printf("%d\n", launder);
    return launder;
}