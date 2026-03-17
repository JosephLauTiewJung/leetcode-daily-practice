from typing import List

'''
time complexity: O(2n)
'''
class Solution:
    @staticmethod
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            sum += nums[right]
            # find the minimal length
            while sum >= target:
                length = right - left + 1
                min_length = min(min_length, length)
                # shrink the window from left to find the minimum length
                sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
