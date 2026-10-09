class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        arr=[]
        arr.append(gain[0])
        a=gain[0]
        for i in range(1,len(gain)):
            a+=gain[i]
            arr.append(a)
        arr.append(0)
        return max(arr)
            

