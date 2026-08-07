class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        y=list(str(abs(x)))
        new=y[::-1]
        res=sign*int("".join(new))
        if res< -2**31 or res>2**31:
            return 0
        return res
        
      