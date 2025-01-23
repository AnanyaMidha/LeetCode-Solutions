class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        n = len(s)
        for i in range(n):
            res +=s[(i+k)%n]
        return res

        