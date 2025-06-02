class Solution(object):
    
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

    # If loop completes, all digits were 9 (e.g., 999 + 1 = 1000)
        return [1] + digits


        