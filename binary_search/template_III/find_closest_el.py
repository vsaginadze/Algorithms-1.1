from typing import List

class Solution:
    def findBoundaries(self, arr: List[int], closest_el_idx: int, cnt: int, x: int) -> (int, int):
        l, r = closest_el_idx-1, closest_el_idx+1

        while cnt:
            if l < 0:
                r += cnt
                break
            
            if r > len(arr)-1:
                l -= cnt
                break
                
            if abs(arr[l] - x) < abs(arr[r] - x): 
                l -= 1
            elif abs(arr[l] - x) == abs(arr[r] - x):
                if arr[l] < arr[r]:
                    l -= 1
                else:
                    r += 1
            else:
                r += 1

            cnt -= 1

        return (l+1, r)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x not in arr:
            if x > arr[-1]:  return arr[len(arr)-k:]
            if x < arr[0]: return arr[:k]
        
        left, right = 0, len(arr)-1
        while left+1 < right:
            mid = (left+right) // 2
            if arr[mid] == x:
                l, r = self.findBoundaries(arr, mid, k-1, x)
                return arr[l:r]
            elif arr[mid] > x:
                right = mid
            else:
                left = mid
        
        if abs(arr[left] - x) == abs(arr[right] - x):
            idx = left if arr[left] < arr[right] else right
        else:
            idx = left if abs(arr[left] - x) < abs(arr[right] - x) else right
        
        l, r = self.findBoundaries(arr, idx, k-1, x)
        return arr[l:r]

arr = [0,1,2,3,4,24,60,80]
k = 5
x = 70

sol = Solution()
closestEls = sol.findClosestElements(arr, k, x)

print(closestEls)