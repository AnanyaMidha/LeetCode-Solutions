class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0       # Number of jumps made so far
        farthest = 0    # The farthest index we can reach in the current jump
        end = 0         # The end index of the current jump range

        # Iterate through the array, except the last element
        for i, num in enumerate(nums[:-1]):
            # Update the farthest position reachable from current or previous steps
            farthest = max(farthest, i + num)

            # If we have reached the end of the range for the current jump
            if i == end:
                jumps += 1          # Make a jump
                end = farthest      # Update the end of the next jump range

        return jumps