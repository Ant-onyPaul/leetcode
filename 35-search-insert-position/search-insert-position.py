class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(len(nums)-1):
            if nums[i]<target and target<nums[i+1]:
                return i+1
        if nums[0]>target:
            return 0
        return len(nums)