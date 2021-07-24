#include <stdio.h>
#include <valgrind/flowcheck.h>

int main(int argc, char ** argv) {
	int h1 = *argv[1];
	FC_TAINT_WORD(&h);
    int h2 = *argv[2];
	FC_TAINT_WORD(&h);
    int h3 = *argv[3];
	FC_TAINT_WORD(&h);


    int l = h1 + h2 + h3;
	printf("%d\n", l);
	return l;
}