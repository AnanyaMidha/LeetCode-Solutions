class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0


        for i in range(0, n):
            yun = len(str(nums[i]))
            if int(yun) % 2 == 0:
                cnt += 1
        return cnt

