class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        summ=0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                summ+=nums[i]**2
        return summ