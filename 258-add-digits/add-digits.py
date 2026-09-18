class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while num>9:
            new=sum(map(int,str(num)))
            num=new
        return num

