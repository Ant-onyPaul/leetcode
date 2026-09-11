class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        for i in range(len(digits)):
            if digits[i]==0:
                continue
            for j in range(len(digits)):
                if j==i:
                    continue
                for k in range(len(digits)):
                    if k==i or k==j:
                        continue
                    if digits[k]%2==0:
                        num=digits[i]*100+digits[j]*10+digits[k]
                        ans.add(num)
        return len(ans)
        # arr=[]
        # ans=[]
        # def dfs(i):
        #     if len(ans)==3:
        #         arr.append(ans[:])
        #     for j in range(i,len(digits)):
        #         ans.append(digits[j])
        #         dfs(j+1)
        #         ans.pop()
        # dfs(0)
        # return len(arr)
