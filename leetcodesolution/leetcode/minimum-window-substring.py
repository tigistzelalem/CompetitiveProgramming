class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count, win_count = {}, {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        have, need = 0, len(t)
        res, resLen = [-1, -1], float('inf')
        l = 0
        indexes = []
        for r in range(len(s)):
            char = s[r]
            win_count[char] = win_count.get(char, 0) + 1

            if char in t_count and win_count[char] <= t_count[char]:
                have += 1
                indexes.append(r)

            if have == need:
                while win_count[s[l]] > t_count.get(s[l], 0) or s[l] not in t_count:
                    win_count[s[l]] -= 1
                    l += 1

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""