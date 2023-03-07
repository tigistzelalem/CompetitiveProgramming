class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_sorted = sorted(map(int, nums), reverse=True)
        return str(nums_sorted[k-1])

                
                
                
            