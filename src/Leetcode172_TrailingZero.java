public class Leetcode172_TrailingZero {
    static void main() {
        trailingZeroes(5);
    }
    public static int trailingZeroes(int n) {
        int count = 0;
        int currentPowerOfFive = 5;
        while (n >= currentPowerOfFive) {
            count += n / currentPowerOfFive;
            currentPowerOfFive *= 5;
        }
        return count;
    }
}
