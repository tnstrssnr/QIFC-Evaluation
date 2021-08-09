// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char ** argv) {
    int h = *argv[1];
	FC_TAINT_WORD(&h);
    int l;
    if (0 <= h && h < 16) {
        l = 3 + h;
    } else {
        l = 3;
    }

    int out = 0;
    for (int i = 0; i != l; ++i) {
        ++out;
    }
    printf("%d\n", l);
    return l;
}