class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        odd_count, ans = 0, 0
        counts[0] = 1

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odd_count += 1
            ans += counts[odd_count - k]
            counts[odd_count] += 1
        
        return ans
       
            





      
