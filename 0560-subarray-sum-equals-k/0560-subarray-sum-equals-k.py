class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = {0:1}
        total = 0
        count = 0
        for i in range(n):
            total += nums[i]
            if total - k in prefix:
                count += prefix[total - k]
            prefix[total] = prefix.get(total, 0) + 1
        return count