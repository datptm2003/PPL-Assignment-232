public class helper {
    public static float modulo(float a, float b)  {
		return a - b * (float)Math.floor(a / b);
	}

	public static String concat(String a, String b) {
		return a + b;
	}

	public static boolean compare(String a, String b) {
		return a.equals(b);
	}
}