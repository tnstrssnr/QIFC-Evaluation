int f(int h) {
    int l;
    if (0 <= h && h < 16) {
			l = h + 3;
		} else {
			l = 3;
		}
    return l;
}