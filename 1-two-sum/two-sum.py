class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in store:
                return [store[comp], i]
            store[nums[i]] = i
            