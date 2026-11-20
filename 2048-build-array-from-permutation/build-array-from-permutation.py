class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(len(nums)):
            arr.append(nums[nums[i]])
        return arr
