class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans=0
        for i in range(len(arr)):
            total=0
            for j in range(i,len(arr)):
                total+=arr[j]
                if (j-i+1)%2==1:
                   ans+=total
        return ans