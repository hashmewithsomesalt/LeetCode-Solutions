class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        mydict = {}
        count = 0
        answer = 0
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count == 0:
                answer = max(i + 1, answer)
                continue
            if count in mydict:
                answer = max(answer, i - mydict[count])
            else:
                mydict[count] = i
            
        return answer