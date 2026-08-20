class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums
        b=nums[::-1]
        
        return a+b
    