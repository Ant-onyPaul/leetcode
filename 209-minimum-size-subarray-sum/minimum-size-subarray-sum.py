class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        summ=0
        minn=float("inf")
        for right in range(len(nums)):
            summ+=nums[right]
            if nums[right]==target:
                return 1
            while summ>=target:
                minn=min(minn,(right-left+1))
                summ-=nums[left]
                left+=1
                
        if sum(nums)<target:
            return 0
        return minn