class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                st.append(char)
            elif char in mapping:
                if not st or st.pop() != mapping[char]:
                    return False
            else:
                return False  #

        return not st