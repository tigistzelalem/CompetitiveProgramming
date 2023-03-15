class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        rigth = len(nums)-1
        while left < rigth:
            if nums[left] + nums[rigth] == k:
                nums.pop(rigth)
                nums.pop(left)
                count +=1
                rigth -=2
            elif nums[left] + nums[rigth] < k:
                left +=1
                
            else:
                rigth -=1
        return count
                
       