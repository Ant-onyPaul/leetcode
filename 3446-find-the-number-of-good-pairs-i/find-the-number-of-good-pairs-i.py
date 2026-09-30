class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count=0
        a=len(nums1)
        b=len(nums2)
        for i in range(a):
            for j in range(b):
                if nums1[i]%(nums2[j]*k)==0 :
                    count+=1
        return count
