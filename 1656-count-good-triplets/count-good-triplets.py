class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if 0<=i and i<j and j<k and k<len(arr):
                        if abs(arr[i] - arr[j])<=a:
                            if abs(arr[j] - arr[k]) <=b:
                                if abs(arr[i] - arr[k]) <= c:
                                    count+=1
        return count
