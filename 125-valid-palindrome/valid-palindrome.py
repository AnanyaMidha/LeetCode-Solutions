class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = ""

        for i in s:
            if i.isalnum():
                str1 += i.lower()
        return str1 == str1[::-1]
        
        