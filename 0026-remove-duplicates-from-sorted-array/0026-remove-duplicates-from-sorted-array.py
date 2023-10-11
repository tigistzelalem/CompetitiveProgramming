class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#             time complexity o(n)
            # i, j = 0, 0
            # while j < len(nums):
            #     if nums[i] == nums[j]:
            #         j +=1
            #     else:
            #         i += 1
            #         nums[i] = nums[j]
            # return i + 1
            k = 1
            for i in range(1,len(nums)):
                isDuplicate = False
                for j in range(k):
                    if nums[i] == nums[j]:
                        isDuplicate = True
                        break
                if not isDuplicate:
                    nums[k] = nums[i]
                    k += 1
            return k