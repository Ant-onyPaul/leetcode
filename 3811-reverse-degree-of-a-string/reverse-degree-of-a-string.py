class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            val=26-(ord(s[i])-ord('a'))
            ans+=(i+1)*val
        return ans