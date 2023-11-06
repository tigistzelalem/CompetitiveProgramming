class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        magical_str = "122"
        ptr = 2
        
        while len(magical_str) < n:
            count = int(magical_str[ptr])
            if magical_str[-1] == '2':
                char = '1'
            else:
                char = '2'
            
            magical_str += char*count
            ptr += 1
        
        return magical_str[:n].count('1')
        