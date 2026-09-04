class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            n=0
            maxx=max(nums[:i+1])
            minn=min(nums[i:])
            n=maxx-minn
            if n<=k:
                return i
        return -1
       