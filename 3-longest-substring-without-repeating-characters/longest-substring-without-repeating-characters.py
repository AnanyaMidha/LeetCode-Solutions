class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set to keep the track of the characters that have been seen
        charSeen = set()
        #two pointers to track the length, left will shrink in case duplicate found, right will expand.
        left, right =0, len(s)
        max_len = 0

        for right in range(len(s)):
            #iss wale mein right pr woh ele aaya h jo left most mein present h abhi
            while s[right] in charSeen:
                charSeen.remove(s[left])
                left+=1
            charSeen.add(s[right])
            max_len = max(max_len, right -left + 1)
        return max_len