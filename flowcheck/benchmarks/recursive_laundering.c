// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int launder(int h, int l) {
    if (h == l) {
        return l;
    }

    return launder(h, l + 1);
}

int main(int arc, char ** argv) {
    int h = *argv[1];
	FC_TAINT_WORD(&h);

    int out = launder(h, 0);
    printf("%d\n", out);
    return out;
}