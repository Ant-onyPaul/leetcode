class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        a=sum(nums)
        b="".join(map(str,nums))
        c=list(map(int,b))
        d=sum(c)
        e=abs(a)-abs(d)
        return e 
        