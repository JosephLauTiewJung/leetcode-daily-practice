public class Leetcode50_Power {
    static void main() {
        System.out.println(myPow(2.0, 10));
    }
    public static double myPow(double x, int n) {
        // eliminate the negative power e.g. 2^-2
        long power = Math.abs((long)n);
        double result = 1;
        while (power != 0) {
            // odd case
            if (power % 2 == 1) {
                result = result * x;
                power = power - 1;
            }
            // even case
            x *= x; // update the base instead of updating the
            power = power / 2;
        }
        return (n < 0 ? 1/result : result);
    }
}
