class Solution:
    def distinctSubseqII(self, s: str) -> int:
        seen={}
        dp=1
        MOD=10**9+7
        for i in s:
            olddp=dp
            dp=dp+olddp
            if i in seen:
                dp-=seen[i]
            seen[i]=olddp
            # dp%=MOD
        return (dp-1)%MOD
            