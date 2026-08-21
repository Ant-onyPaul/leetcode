class Solution:
    def maxPower(self, s: str) -> int:
        left=0
        count=1
        ans=1
        for right in range(1,len(s)):
            if s[right]==s[left]:
                count+=1
            else:
                count=1
            ans=max(ans,count)
            left+=1
        return ans
