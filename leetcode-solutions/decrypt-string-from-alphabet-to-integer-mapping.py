class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        right = len(s) - 1
        while right >= 0:
            if s[right] == '#':
                num = int(s[right-2: right])
                print(num)
                ans = (chr(ord('a') + num - 1)) + ans
                right -= 3
            else:
                num = int(s[right])
                ans = (chr(ord('a') + num - 1)) + ans
                right -= 1

        return ans