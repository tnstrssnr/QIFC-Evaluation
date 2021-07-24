int f(int h1) {
    int launder = 0;
		int shift = 1;
		int i = 0;

		while (i != h1) {
			launder += 1;
			shift = shift << 1;
			i++;
		}
    return launder;
}