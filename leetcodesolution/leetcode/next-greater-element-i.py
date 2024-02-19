class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict_ = {}

        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    popped = stack.pop()
                    dict_[popped] = nums2[i]
                stack.append(nums2[i])

        result = []
        for i in range(len(nums1)):
            if nums1[i] not in dict_:
                dict_[nums1[i]]  = -1
            result.append(dict_[nums1[i]])

        return result
            
