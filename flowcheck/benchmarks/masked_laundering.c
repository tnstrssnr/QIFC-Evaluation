#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char** argv) {
    int h = *argv[1];
	FC_TAINT_WORD(&h);

    int out = 0;

    while (out != h) {
        out++;
    }
    if ((h & 1) != 0) {
        out = 1;
    }
    printf("%d\n", out);
    return out;
}