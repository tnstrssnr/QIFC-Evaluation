// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int id(int i) {
    int r = 0;
    if ( i > 0 ) {
        r = id(i - 1) + 1;
    }
    return 0;
}


int main(int argc, char **argv) {
    int h = *argv[1];
    FC_TAINT_WORD(&h);
    int l = id(h);
    printf("%d\n", l);
}