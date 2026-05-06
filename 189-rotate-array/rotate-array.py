class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k %= n

        #reverse the entire array

        nums.reverse()

        #reverse first k elemnets

        nums[:k] = reversed(nums[:k])

        #Reverse remaining

        nums[k:] = reversed(nums[k:])


        