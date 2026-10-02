class Solution:
    def maximum69Number (self, num: int) -> int:
        arr=list((map(int,str(num))))
        for i in range(len(arr)):
            if arr[i] != 9:
                arr[i] = 9
                break
        return int("".join(map(str,arr)))