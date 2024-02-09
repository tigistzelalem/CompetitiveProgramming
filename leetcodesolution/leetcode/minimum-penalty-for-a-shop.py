class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre_sum = [0]*(len(customers) + 1)
        suff_sum = [0]*(len(customers) + 1)

        for i, char in enumerate(customers):
            if char == "N":
                pre_sum[i] += 1
            if char == "Y":
                suff_sum[i] += 1
                
        pr = pre_sum.copy()
        acc = 0
        for i in range(len(pre_sum)):
            pre_sum[i] = acc
            acc += pr[i]

        acc = 0
        for i in range(len(suff_sum)-1,-1,-1):
            acc += suff_sum[i]
            suff_sum[i] = acc
            pre_sum[i] += suff_sum[i]
        
        min_ = min(pre_sum)

        return pre_sum.index(min_)            

        