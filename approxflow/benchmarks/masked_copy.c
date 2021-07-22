int f(int h) {
    int l = h & (-1 << 16);
    return l;
}