class Solution:
    def minimumAbsDifference(self, lst: List[int]) -> List[List[int]]:
        shift = min(lst)
        K = max(lst) - shift
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem - shift] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            sorted_lst[counts[elem - shift]] = elem
            counts[elem - shift] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
        print(sorted_lst)

        differences = []
        for i in range(len(lst)-1):
            differences.append(lst[i+1]-lst[i])

        pairs = []
        min_difference = min(differences)

        for i in range(len(differences)):
            if differences[i] == min_difference:
                pairs.append([lst[i], lst[i+1]])

        return pairs



