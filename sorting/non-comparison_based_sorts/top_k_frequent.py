class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        # Step 2: Create buckets
        max_freq = max(freq_map.values())
        buckets = [[] for _ in range(max_freq + 1)]

        # Step 3: Populate buckets
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 4: Collect k most frequent elements
        result = []
        for i in range(max_freq, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break

        return result[:k]
