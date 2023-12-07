class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      included = set()
      for start, end in ranges:
        for i in range(start, end + 1):
          included.add(i)

      for i in range(left, right + 1):
        if i not in included:
          return False

      return True


     