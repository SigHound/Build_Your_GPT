class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        ans = [0] * numsLen * 2
        for i in range (len(ans)):
            ans[i] = nums[i % numsLen]
        return(ans)