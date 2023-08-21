class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        sub_str = []

        for i in range(len(s) - 2):
            sub = s[i:i+3]
            sub_str.append(sub)
            
        count = 0
        for substring in sub_str:
                if (len(set(substring)) == len(substring)):
                    count += 1
        return count
                