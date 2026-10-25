class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        out=999
        for i in range(len(tasks)):
            a=sum(tasks[i])
            out=min(a,out)
        return out
    
