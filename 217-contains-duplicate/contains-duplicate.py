class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        count = {}

        for i in nums:
            # Initialize the count for the element if it doesn't exist
            if i not in count:
                count[i] = 0
            count[i] += 1
            if count[i] > 1:
                return True
        return False
