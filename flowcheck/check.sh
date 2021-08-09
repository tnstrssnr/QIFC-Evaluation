gcc -m32 $1 -o $2 -I/flowcheck-1.20/include
flowcheck-1.20/bin/valgrind --tool=exp-flowcheck  $2 $3