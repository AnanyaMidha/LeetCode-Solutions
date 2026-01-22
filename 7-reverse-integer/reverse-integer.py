class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        int_min, int_max = -2**31, 2**31 - 1

        while x:
            if rev_num < int_min // 10 + 1 or   rev_num > int_max // 10:
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10 
            rev_num = rev_num * 10 + digit

            x = (x - digit) // 10

        return rev_num