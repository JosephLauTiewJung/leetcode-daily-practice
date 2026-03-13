public class Leetcode136_SingleNumber {
    static void main() {
        int[] nums = {2, 2, 1};
        System.out.println(Solution.singleNumber(nums));
    }
    static class Solution {
        public static int singleNumber(int[] nums) {
            // use bit wise operator
            int singleNumber = 0;
            for (int num : nums) {
                singleNumber = singleNumber ^ num;
            }
            return singleNumber;
        }
    }
}