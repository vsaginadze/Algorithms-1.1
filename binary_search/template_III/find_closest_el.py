from typing import List

class Solution:
    def findBoundaries(self, arr: List[int], closest_el: int) -> (int, int):
        pass

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x not in arr:
            if x > arr[-1]:  return arr[len(arr)-k:]
            if x < arr[0]: return arr[:k]
        
        left, right = 0, len(arr)-1
        while left+1 < right:
            mid = (left+right) // 2
            if arr[mid] == x:
                l, r = self.findBoundaries(self, arr, mid)
                return arr[l:r]
            elif arr[mid] > x:
                right = mid
            else:
                left = mid
        
        if abs(left - x) == abs(right - x):
            closest_el = min(left, right)
        else:
            closest_el = min(left, right, key=lambda num: (abs(num - x), num))
        
        l, r = self.findBoundaries(arr, closest_el)
        return arr[l:r]

arr = [0,1,24,70,100,150]
k = 3
x = 70

sol = Solution()
closestEls = sol.findClosestElements(arr, k, x)

print(closestEls)