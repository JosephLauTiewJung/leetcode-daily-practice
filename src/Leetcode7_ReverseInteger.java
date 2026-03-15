public class Leetcode7_ReverseInteger {
    static void main() {
    }
    public static int reverse(int x) {
        int MAX = Integer.MAX_VALUE;
        int MIN = Integer.MIN_VALUE;
        if (x > MAX || x < MIN) return 0;

        int reverse = 0;
        while (x != 0) {
            if (reverse < MIN / 10 || reverse > MAX / 10) return 0;
            // update reverse
            reverse = (reverse * 10) + (x % 10);
            // update x
            x = x / 10;
        }
        return reverse;
    }
}
