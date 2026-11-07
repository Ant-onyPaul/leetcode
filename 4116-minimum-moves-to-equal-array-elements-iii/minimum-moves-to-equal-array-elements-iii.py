class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        a=max(nums)
        ans=0
        nums.pop(-1)
    
        for i in range(len(nums)):
            ans+=a-nums[i]
        return ans
        