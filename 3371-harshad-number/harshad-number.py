class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=sum(map(int,str(x)))
        if x%a==0:
            return a
        return -1
