class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sorted_task = sorted(tasks)
        processorTime.sort()
        n = len(processorTime)
        m = len(tasks)
        max_num = float('-inf')
        ans = float('-inf')
        j = 0
        for i in range(0,n):
            max_num = max(sorted_task[j:j + 4])
            j += 4
            ans = max(ans, max_num + processorTime[n-i-1])

        return ans



