class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mpST, mpTS = {}, {}

        for c1, c2 in zip(s, t):

            if((c1 in mpST and mpST[c1] != c2) or (c2 in mpTS and mpTS[c2] != c1)):
                return False
            mpST[c1] = c2
            mpTS[c2] = c1
        return True
        