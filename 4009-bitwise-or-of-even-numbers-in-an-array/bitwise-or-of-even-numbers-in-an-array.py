class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            if i%2==0:
                arr.append(i)
        out=0
        for i in arr:
            out|=i
        return out