class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        min_ele = min(strs)
        max_ele = max(strs)
        for i in range(len(min_ele)):
            if min_ele[i] != max_ele[i]:
                return min_ele[0:i]
        return min_ele