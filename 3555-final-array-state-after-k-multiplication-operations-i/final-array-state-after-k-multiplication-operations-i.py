class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            x=min(nums)
            index=nums.index(x)
            nums[index]=nums[index]*multiplier
        return nums
        
            