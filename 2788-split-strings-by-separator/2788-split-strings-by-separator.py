class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        res = []
        for word in words:
            for val in word.split(separator):
                if val:
                    res.append(val)
        return res
            