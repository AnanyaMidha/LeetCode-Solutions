class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, c in count.items():
            if c > n // 3:
                res.append(num)

        return res
            