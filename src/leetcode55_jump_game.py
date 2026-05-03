from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        # use greddy algorithm 
        max_range = 0
        # track the maximum range that each index can reach
        for i in range(0, len(nums)): 
            # for the case that num[i] is 0
            if i > max_range: 
                return False
            max_range = max(max_range, i + nums[i])
            print(f'max_range: {max_range}')
        # if the maximum range can reach the last index, return true
            if max_range >= len(nums) - 1: 
                return True 
        # else return false
        return False 
if __name__ == '__main__': 
    nums = [3,2,1,0,4]
    solution = Solution()
    print(solution.canJump(nums=nums))