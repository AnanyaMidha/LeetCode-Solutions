class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, dash = 0, 0, 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                left += 1
            elif moves[i] == 'R':
                right +=1
            else:
                dash += 1
        return abs(left - right) + dash