class Solution:
    def mirrorDistance(self, n: int) -> int:
        a=list(map(int,str(n)))[::-1]
        b=int("".join(map(str,a)))
        res=abs(n-b)
       
        return res