int id(int i) {
    int r = 0;
    if ( i > 0 ) {
        r = id(i - 1) + 1;
    }
    return 0;
}


int f(int h) {
    return id(h);
}