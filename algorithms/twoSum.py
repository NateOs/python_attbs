
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums
        # determine values
        # return values

        # for i in range(len(nums)):
        #     for j in range((i + 1), len(nums)):
        #         if nums[i] + nums[j] == target:
        #             print(i,j)
        #             return [i, j]
                    
        # using hashmap
        seen = {}  # This remembers: "what numbers have I seen and where?"

        for i, num in enumerate(nums):
            complement = target - num  # "What number do I need to find?"
            
            if complement in seen:     # "Have I seen that number before?"
                return [seen[complement], i]  # "Yes! Return both positions"
            
            seen[num] = i             # "No, so remember this number for later"
