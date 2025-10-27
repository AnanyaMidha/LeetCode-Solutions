class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0 # this will move to the next non zero elemnet

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
                lastNonZero += 1
        