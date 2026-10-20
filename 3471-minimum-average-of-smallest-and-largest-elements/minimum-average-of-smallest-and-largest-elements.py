class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        nums.sort()
        a=len(nums)//2
        for i in range(a):
            minn=nums.pop(0)
            maxx=nums.pop(-1)
            av=(minn+maxx)/2
            avg.append(av)
        return min(avg)