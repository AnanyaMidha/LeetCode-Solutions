class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_index = 0
      
        # Iterate through each element in the array
        for num in nums:
            # If current element is not the value to be removed
            if num != val:
                # Place it at the valid_index position
                nums[valid_index] = num
                # Move the valid_index pointer forward
                valid_index += 1
      
        # Return the count of elements that are not equal to val
        return valid_index  