int launder(int h, int l) {
    if (h == l) {
        return l;
    }

    return launder(h, l + 1);
}

int f(int h) {
    int out = launder(h, 0);
    return out;
}