from typing import List

class Solution:
    def findKthLargest(self, lst: List[int], k: int) -> int:
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[largest], lst[index] = lst[index], lst[largest]
                max_heapify(heap_size, largest)
        
    
        # max heapify the list
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)
        
        for i in range(len(lst)-1,len(lst)-k-1,-1):
            # swap largest(first) element with the last
            lst[i], lst[0] = lst[0], lst[i]
            # notice that we reduce the lst size by one on each iteration
            max_heapify(i, 0)

        return lst[len(lst)-k]

sol = Solution()
arr = [3,2,1,5,6,4] 
k = 2

arr = sol.findKthLargest(arr, k)
print(arr)