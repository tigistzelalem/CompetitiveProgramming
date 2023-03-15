class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in nums1:
            ans = -1
            index = nums2.index(i)
            temp = nums2[index+1:]
            for j in temp:
                if j > i:
                    ans = j
                    break
            stack.append(ans)
        return stack
                
                        
            

