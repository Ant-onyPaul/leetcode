class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        left=1
        arr=[]
        right=len(height)-1
        while left<=right:
            if height[left-1]>threshold:
                arr.append(left)
            left+=1
        return arr