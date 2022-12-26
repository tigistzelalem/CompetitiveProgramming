class Solution:
    def sortSentence(self, s: str) -> str:
        words = s[::-1].split()
        words.sort()
        list =[]
        print(words)
        for word in words:
            text = word[::-1]
            text = text[:-1]
            list.append(text)
        return ' ' .join(list)
            
            
        
       
