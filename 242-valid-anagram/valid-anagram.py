class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alpha = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        for val in alpha:
            if val != 0:
                return False
        return True
        
        
        