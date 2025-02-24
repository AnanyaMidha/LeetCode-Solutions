class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 1 or n == 7):
            return True
        elif(n < 10):
            return False
        else:
            summ = 0
            while (n > 0):
                temp = n % 10
                summ += temp * temp
                n = n // 10
            return self.isHappy(summ)

        