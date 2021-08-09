// 0
#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char ** argv) {
	int h = *argv[1];
	FC_TAINT_WORD(&h);

    int parity = 0;
    int bitSet;

    for (int j = 0; j != 32; ++j) {
        int bit = h & (1 << j);
        if (bit != 0) {
            bitSet = 1;
        } else {
            bitSet = 0;
        }
        if (bitSet != parity) {
            parity = 1;
        } else {
            parity = 0;
        }
    }
    printf("%d\n", parity);
    return parity;
}