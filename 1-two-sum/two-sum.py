class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}

        for i, num in enumerate(nums):
            complement = target - num
            if(complement in store):
                return [store[complement], i]
            store[num] = i
        return
        