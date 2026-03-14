public class Leetcode9_Palindrome {
    static void main() {
        Solution.isPalindrome(121);
    }
    static class Solution {
        public static boolean isPalindrome(int x) {
            if (x < 0 || x % 10 == 0) {
                return false;
            }
            int reverse = 0;
            while (x > reverse) {
                int lastDigit = x % 10;
                reverse = reverse * 10 + lastDigit;
                x = x / 10;
            }
            System.out.println(x);
            System.out.println(reverse);
            return (x == reverse) || (x == reverse / 10);
        }
    }
}
