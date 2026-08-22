class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        product=1
        st=str(n)
        for i in range(len(st)):
            summ+=int(st[i])
            product*=int(st[i])
        if n%(summ + product) == 0:
            return True
        return False

        