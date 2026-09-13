class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                subst=s[i:j+1]
                if subst == subst[::-1]:
                    if len(subst)>len(ans):
                        ans=subst
        return ans