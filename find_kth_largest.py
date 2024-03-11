from typing import List

class Solution:
    def findKthLargest(self, lst: List[int], k: int) -> int:
        for i in range(k+1):
            max_index = i
            for j in range(i + 1, len(lst)):
                # Update minimum index
                if lst[j] > lst[max_index]:
                    max_index = j

            # Swap current index with minimum element in rest of list
            lst[max_index], lst[i] = lst[i], lst[max_index]
        
        return lst[k]

sol = Solution()
arr = [3,2,1,5,6,4] 
k = 2

arr = sol.findKthLargest(arr, k)
print(arr)