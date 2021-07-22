int f(int h) {
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
    return l;
}