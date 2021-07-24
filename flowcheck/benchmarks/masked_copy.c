#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argv, char ** argc) {
    int h = *argv[1];
	FC_TAINT_WORD(&h);

    int l = h & (-1 << 16);
    printf("%d\n", l);
    return l;
}