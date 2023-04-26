class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def play(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            score_if_pick_left = nums[i] + min(play(i+2, j), play(i+1, j-1))
            score_if_pick_right = nums[j] + min(play(i, j-2), play(i+1, j-1))
            memo[(i, j)] = max(score_if_pick_left, score_if_pick_right)
            return memo[(i, j)]

        total_score = sum(nums)
        player1_score = play(0, n-1)
        return player1_score >= (total_score + 1) // 2