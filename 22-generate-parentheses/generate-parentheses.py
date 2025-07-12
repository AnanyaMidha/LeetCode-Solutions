class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backTrack(curr, open_count, close_count):
            if len(curr) == 2*n:
                result.append(curr)
                return 
            if open_count < n:
                backTrack(curr + '(', open_count + 1, close_count)
            if close_count < open_count:
                backTrack(curr + ')', open_count, close_count + 1)
        backTrack("", 0, 0)
        return result