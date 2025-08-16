class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini, maxi = 0, 0
        
        #to find the mini and the maxi elements from the array 

        for i, num in enumerate(nums):
            if num < nums[mini]:
                mini = i
            if num > nums[maxi]:
                maxi = i
        if mini > maxi:
            mini, maxi = maxi, mini
        return min(maxi + 1, len(nums) - mini, mini + 1 + len(nums) - maxi)