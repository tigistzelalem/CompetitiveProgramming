class NumArray:

    def __init__(self, nums: List[int]):
        self.result=[0]*len(nums)
        count=0
        for i in range(len(nums)):
            count+=nums[i]
            self.result[i]+=count
       
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.result[right]
        return self.result[right]-self.result[left-1]    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)