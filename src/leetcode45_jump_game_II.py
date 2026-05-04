from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # start from 0-indexed, can jump to i + j, where j = num[i]
        # minimum jump to n - 1 
        # can use greedy_algorithm, find the maximum range reachable 
        farthest = 0
        current_end = 0
        jumps = 0
        for i in range(0, len(nums) - 2): 
            # find the farthest distance
            farthest = max(farthest, nums[i] + i)

            # if we reach the current end, which means that we haven't reach the 
            # end of the array first. We need to add 1 jump 
            if i == current_end: 
                # what is the farthest distance taht I can reached from this position? 
                current_end = farthest 
                jumps += 1

        return jumps 
        
if __name__ == '__main__': 
    solution = Solution()
    print(solution.jump(nums=[2,3,1,1,4]))