class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        count = 0
        for num in reversed(s):
            if num == "0":
                count += 1
            else:
                ans += count

        return ans
