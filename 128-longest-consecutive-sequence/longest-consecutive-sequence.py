class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current=1
        longest=1
        zero=0
        if nums==[]:
            return zero
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-nums[i-1]==1:
                current+=1
            else:
                longest=max(longest,current)
                current=1
        longest=max(longest,current)
        return longest


