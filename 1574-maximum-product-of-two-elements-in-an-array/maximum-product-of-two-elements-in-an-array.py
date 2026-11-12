class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxx=0
        nums.sort()
        for i in range(len(nums)-1):
            a=(nums[i]-1)*(nums[i+1]-1)
            maxx=max(maxx,a)
        return maxx