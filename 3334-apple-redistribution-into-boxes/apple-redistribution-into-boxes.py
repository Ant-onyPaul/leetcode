class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total=sum(apple)
        a=1
        b=0
        capacity.sort(reverse=True)
        for i in range(len(capacity)):
            b+=capacity[i]
            if b>=total:
                return a
            else:
                a+=1
        
           

