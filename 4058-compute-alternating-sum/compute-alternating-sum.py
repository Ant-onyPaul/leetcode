class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(0,len(nums),2):
            a+=nums[i]
        for i in range(1,len(nums),2):
            b+=nums[i]
        return a-b