class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()  # remove leading whitespaces
        if not s:
            return 0

        res = 0
        sign = 1
        i = 0

    # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

    # Convert characters to digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + (ord(s[i]) - ord('0'))
            i += 1

        res *= sign

    # Clamp the result to 32-bit signed int range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res
        

        