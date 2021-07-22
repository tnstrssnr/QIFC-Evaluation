int f(int h) {
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
    return parity;
}