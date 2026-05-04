from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # start from 0-indexed, can jump to i + j, where j = num[i]
        # minimum jump to n - 1 
        # can use greedy_algorithm, find the maximum range reachable 
        farthest = 0
        current_end = 0
        jumps = 0
        # edge case: only have one element 
        if len(nums) == 1: 
            return 0
        for i in range(0, len(nums) - 1): 
            # find the farthest distance
            farthest = max(farthest, nums[i] + i)
            print(f'fartheset: {farthest}')
            # if we reach the current end, which means that we haven't reach the 
            # end of the array first. We need to add 1 jump 
            if i == current_end: 
                current_end = farthest
                print(f'current_end: {current_end}')
                jumps += 1
                print(f'jump: {jumps}')

        return jumps
        
if __name__ == '__main__': 
    solution = Solution()
    print(solution.jump(nums=[1,2]))