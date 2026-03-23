from typing import List

# time complexity: O(log(n))
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums) - 1
        while lower <= higher: 
            middle = lower + (higher - lower) // 2
            if nums[middle] == target: 
                return middle
            elif nums[middle] < target: 
                lower = middle + 1
            elif nums[middle] > target: 
                higher = middle - 1
            
        return -1
