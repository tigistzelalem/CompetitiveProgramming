class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        number = int(num)
        j = 0
        if number % 10 == 0:
            reverseNum = num[::-1]
            
            for i in reverseNum:
                if i == '0':
                    j = j + 1
            
                else:
                    finalNum = reverseNum[j:]
                    finalNum = finalNum[::-1]
                    return finalNum
        else:
            return num