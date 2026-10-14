class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        c=1
        a=sum(map(int,str(n)))
        b=list(map(int,str(n)))
        for i in b:
            c*=i
        return c-a
        