import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] =- nums[i]

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
        