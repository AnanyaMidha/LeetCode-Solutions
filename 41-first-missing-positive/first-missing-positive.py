class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive = set()

        for num in nums:
            if num > 0:
                positive.add(num)

        ans = 1

        while ans in positive:
            ans += 1

        return ans
        