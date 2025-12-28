class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in store:
                return [i, store[complement]]
            store[num] = i
        return