from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        char_count = Counter(magazine)
        for char in ransomNote:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        return True



        