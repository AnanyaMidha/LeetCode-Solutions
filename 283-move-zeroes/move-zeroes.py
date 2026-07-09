class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        LNZ = 0 #this will point to the next non zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[LNZ] = nums[LNZ], nums[i]
                LNZ += 1