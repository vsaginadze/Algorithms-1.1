from typing import List

class Solution:
    def sortArray(self, lst: List[int]) -> List[int]:
        # Mutates elements in the list by utilizing the heap data structure
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

        # use heap to sort elements
        for i in range(len(lst)-1,0,-1):
            # swap largest(first) element with the last
            lst[i], lst[0] = lst[0], lst[i]
            # notice that we reduce the lst size by one on each iteration
            max_heapify(i, 0)
        
        return lst