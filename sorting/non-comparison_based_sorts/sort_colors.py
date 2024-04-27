class Solution:
    def sortColors(self, nums: List[int]) -> None:
        K = max(nums)
        counts = [0] * (K + 1)
        for elem in nums:
            counts[elem] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(nums)

        for elem in nums:
            sorted_lst[counts[elem]] = elem
            counts[elem] += 1

        for i in range(len(nums)):
            nums[i] = sorted_lst[i]
