int f(int h) {
    int out = 0;

    while (out != h) {
        out++;
    }
    if ((h & 1) != 0) {
        out = 1;
    }
    return out;
}