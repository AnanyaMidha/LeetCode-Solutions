class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 0:
            return
        k = k % n

        if k > n:
            return
        temp = nums[n - k:]
        
        for i in range(n - k - 1, - 1, -1 ):

            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = temp [i] 

        