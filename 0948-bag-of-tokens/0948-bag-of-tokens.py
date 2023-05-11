class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        max_ans, score = 0,0
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                max_ans = max(max_ans, score)
                left += 1
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return max_ans
                    