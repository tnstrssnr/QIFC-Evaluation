#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char **argv) {
    int h = *argv[1];
    FC_TAINT_WORD(&h);
    printf("%d\n", h);
}