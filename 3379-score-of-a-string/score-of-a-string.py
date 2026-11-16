class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for i in range(len(s)-1):
            a=ord(s[i])
            b=ord(s[i+1])
            res+=abs(a-b)
        return res