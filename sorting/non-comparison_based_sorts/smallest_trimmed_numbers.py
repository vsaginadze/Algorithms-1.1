from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for pair in queries:
            k, trim = pair
            arr = [(int(num[-trim:]), i) for i, num in enumerate(nums)]
            print(arr)
            result.append[arr[k-1][1]]
        return result
