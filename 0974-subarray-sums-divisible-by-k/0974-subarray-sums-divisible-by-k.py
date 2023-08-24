class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        premod = 0
        ans = 0
        
        mod_ = [0]*k
        mod_[0] = 1
        
        for num in nums:
            premod = (premod + num % k + k) % k
            ans += mod_[premod]
            
            mod_[premod] += 1
        return ans