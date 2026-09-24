class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=sum(map(int,str(nums[i])))
            if n == i:
                return i
        return -1