from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        diffs = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            diffs.append(nums[i+1]-nums[i])
        return max(diffs)
