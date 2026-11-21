class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        answer = 0
        netgain = [0] * (n + 1)
        for i in range(n):
            netgain[i + 1] = netgain[i] + gain[i]
            answer = max(netgain[i + 1], answer)
        return answer  