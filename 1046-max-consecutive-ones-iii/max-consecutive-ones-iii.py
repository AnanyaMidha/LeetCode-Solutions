class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxLen, num_zeros = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            w = r - l + 1

            maxLen = max(maxLen, w)
        return maxLen
