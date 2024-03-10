from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        has_swapped = True
        mismatches = 0
        expected = [i for i in heights]
        while has_swapped:
            has_swapped = False
            for i in range(len(expected)-1):
                if expected[i] > expected[i+1]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    has_swapped = True

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatches += 1
        
        return mismatches
        

heights = [5,1,2,3,4]
sol = Solution()
sol.heightChecker(heights)