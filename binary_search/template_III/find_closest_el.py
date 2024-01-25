from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x not in arr:
            if x > arr[-1]:
                return arr[len(arr)-4:]
            if x < arr[0]:
                return arr[:k]
        
        closest_el = -1
        left, right = 0, len(arr)-1

        while left+1 < right:
            mid = (left+right) // 2
            if arr[mid] == x:
                closest_el = mid
                break
            elif abs(arr[mid] - x) == abs(arr[right] - x):
                if left < right:
                    right = mid
                else:
                    left = mid
            elif abs(arr[mid] - x) < abs(arr[right] - x):
                right = mid
            else:
                left = mid
        
        if closest_el == -1:
            if abs(left - x) < abs(right - x):
                closest_el = left
            elif abs(left - x) == abs(right - x):
                closest_el = min(left, right)
            else:
                closest_el = right
        


        print(left,right, closest_el)

arr = [0,1,2,3,24,125,126]
k = 3
x = 70
sol = Solution()
sol.findClosestElements(arr, k, x)
# expected answer -> [24, 125, 126]
'''
[0,1,2,3,24,125,126]

5 -> num of els
3 -> item
res -> [0, 2, 3, 4, 5]

# pre-processing
if not item in arr:
    if item > arr[len(arr)-1]:
        return arr[len(arr)-k:]
    if item < arr[0]:
        return arr[:k]

# binary search
finds the item 3
    leftSearch = 2
    rightSearch = 4


'''