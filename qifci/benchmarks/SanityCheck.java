// 0
// 1
// 17
import edu.kit.joana.ifc.sdg.qifc.qif_interpreter.input.Out;

public class SanityCheck {

	public static void main(String[] args) {
		new SanityCheck().sanityCheck(0);
	}

	public void sanityCheck(int h) {
		int l;
		if (0 <= h && h < 16) {
			l = h + 3;
		} else {
			l = 3;
		}
		Out.print(l);
	}
}