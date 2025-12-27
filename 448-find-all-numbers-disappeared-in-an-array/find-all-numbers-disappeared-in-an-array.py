class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bun = set(nums)
        missing = []

        for i in range(1, len(nums) + 1):
            if i not in bun:
                missing.append(i)
        return missing