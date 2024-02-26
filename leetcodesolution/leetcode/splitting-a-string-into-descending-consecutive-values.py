class Solution:
    def splitString(self, s: str) -> bool:
        curr = []
        def split(idx):
            if idx >= len(s):
                return len(curr) >= 2

            
            for i in range(idx, len(s)):
                val = int(s[idx: i+1])
                
                if len(curr) == 0 or val == curr[-1] - 1:
                    curr.append(val)
                    if split(i+1):

                        return True
                    curr.pop()

            return False
        return split(0)
