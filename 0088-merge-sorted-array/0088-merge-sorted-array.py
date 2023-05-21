class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        if n == 0:
            return
        p1 = 0
        p2 = 0
        arr = []
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
            else:
                arr.append(nums2[p2])
                p2 +=1
        for i in range(p1, m):
            arr.append(nums1[i])
        for i in range(p2, n):
            arr.append(nums2[i])
        nums1[:] = arr[:]