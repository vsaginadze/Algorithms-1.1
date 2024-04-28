from typing import List

class Solution:
    def smallestTrimmedNumbers(self, lst: List[str], queries: List[List[int]]) -> List[int]:
        results = []
        for pair in queries:
            min, trim = pair

            counts = [0] * 10

            for el in lst:
                digit = int(el[-trim])
                counts[digit] += 1
        
            # starting_index = 0
            # for i, count in enumerate(counts):
            #     counts[i] = starting_index
            #     starting_index += count
            
            
            # sorted_lst = [0] * len(lst)
            # for elem in lst:
            #     digit = int(el[-trim])
            #     sorted_lst[counts[digit]] = elem
            #     counts[digit] += 1
            


lst = ["64333639502","65953866768","17845691654","87148775908","58954177897","70439926174","48059986638","47548857440","18418180516","06364956881","01866627626","36824890579","14672385151","71207752868"]
queries = [[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]

sol = Solution()
sol.smallestTrimmedNumbers(lst, queries)

'''
nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
k_th, trim = pair -> [1,1]

1. crop `trim` numbers from behind to every nums element
arr -> ["2", "3", "1", "4"]

2. find k_th number in arr

3. get index of arr[k_th] in nums

'''