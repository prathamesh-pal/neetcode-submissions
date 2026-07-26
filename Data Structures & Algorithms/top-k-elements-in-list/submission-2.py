class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # k most frequent elements
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res