class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        a = sorted(counter, key=counter.get, reverse=True)

        return a[:k]

