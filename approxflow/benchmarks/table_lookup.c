int f(int h) {
    int table[8];
    table[0] = 0;
    table[1] = 1;
    table[2] = 2;
    table[3] = 3;
    table[4] = 4;
    table[5] = 5;
    table[6] = 6;
    table[7] = 7;

    int l = 0;

    if (0 <= h && h < 8) {
        l = table[h];
    }

    return l;
}