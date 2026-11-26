class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs[0]) == 0 or len(strs[-1]) == 0:
            return ""
        strs.sort()
        answer = ""

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return answer
            answer += strs[0][i]
        return answer