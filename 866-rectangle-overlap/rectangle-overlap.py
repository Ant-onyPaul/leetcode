class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,x2,y1,y2=rec1
        a1,a2,b1,b2=rec2
        if y1<=a1 or b1<=x1:
            return False
        if y2<=a2 or b2<=x2:
            return False
        return True