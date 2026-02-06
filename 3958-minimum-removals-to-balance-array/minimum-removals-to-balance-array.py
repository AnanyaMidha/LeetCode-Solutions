class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_len = 0
        n = len(nums)

        for right in range(n):
            # Move left pointer while window is invalid
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len