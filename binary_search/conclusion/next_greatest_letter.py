from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target not in letters:
            if letters[0] > target or target > letters[-1]: 
                return letters[0]
            
        if target == letters[-1]: return letters[0]
        
        left, right = 0, len(letters)-1
        while left+1 < right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if letters[mid+1] == target:
                    left = mid
                else:
                    return letters[mid+1]
            elif target < letters[mid]:
                right = mid
            else:
                left = mid
        
        return letters[max(left, right)]


