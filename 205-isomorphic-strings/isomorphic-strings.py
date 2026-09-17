class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]
            if a in st and st[a]!=b:
                return False
            if b in ts and ts[b]!=a:
                return False
            st[a]=b
            ts[b]=a
        return True
        