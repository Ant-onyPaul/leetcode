class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]<target:
                    count+=1
        return count