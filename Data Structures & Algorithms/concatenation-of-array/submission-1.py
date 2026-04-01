class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        ansLen = numsLen * 2
        ans=[]
        for i in range (ansLen):
            ans.append(nums[i % numsLen])
        return(ans)