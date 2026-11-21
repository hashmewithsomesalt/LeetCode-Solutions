class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        answer = 0
        netgain = 0
        for i in range(n):
            netgain = netgain + gain[i]
            answer = max(netgain, answer)
        return answer  