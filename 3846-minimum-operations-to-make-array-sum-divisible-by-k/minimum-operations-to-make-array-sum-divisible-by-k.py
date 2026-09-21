class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums) % k==0:
            return 0
        n=sum(nums)
        return n%k