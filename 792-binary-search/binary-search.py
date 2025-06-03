class Solution(object):
    def recursive(self, nums, low, high, target):
        if low > high:
            return - 1
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.recursive(nums, low, mid - 1, target)
        else:
            return self.recursive(nums, mid + 1, high, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left, right = 0, len(nums) - 1

        # while left <= right:
        #     mid = (left + right)//2
        #     if(nums[mid] == target):
        #         return mid
        #     elif(nums[mid] < target):
        #         left = mid + 1
        #     elif(nums[mid] > target):
        #         right = mid - 1
        # return -1
        # Recursive code:
        return self.recursive(nums, 0, len(nums) - 1, target)


            
            
        