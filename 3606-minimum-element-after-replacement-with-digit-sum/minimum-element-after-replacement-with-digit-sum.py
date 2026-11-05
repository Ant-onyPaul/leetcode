class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            a=sum(map(int,str(nums[i])))
            arr.append(a)
        return min(arr)