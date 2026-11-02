class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=0
        countt=0
        
        for i in nums1:
            if i in nums2:
                count+=1
        for i in nums2:
            if i in nums1:
                countt+=1
        return [count,countt]