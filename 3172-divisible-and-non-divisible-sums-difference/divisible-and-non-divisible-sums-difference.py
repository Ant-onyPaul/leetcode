class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div=[]
        nondiv=[]
        i=1
        while i <= n:
            if i % m == 0:
                div.append(i)
            else:
                nondiv.append(i)
            i+=1
        a=sum(div)
        b=sum(nondiv)
        c=b-a
        return c
