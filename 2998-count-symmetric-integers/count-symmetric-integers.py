class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        while low<=high:
            s=str(low)
            if len(s)%2==0:
                mid=len(s)//2
                first=sum(map(int,s[:mid]))
                second=sum(map(int,s[mid:]))
                if first == second:
                    count+=1
            low+=1
        return count