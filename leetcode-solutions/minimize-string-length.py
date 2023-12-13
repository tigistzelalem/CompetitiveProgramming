class Solution:
    def minimizedStringLength(self, s: str) -> int:
        sets = set()
        for i in s:
            if i not in sets:
                sets.add(i)

        return len(sets)