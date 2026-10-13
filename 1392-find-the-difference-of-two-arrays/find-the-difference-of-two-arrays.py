class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        arr1 = []
        arr2 = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in arr1:
                arr1.append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in arr2:
                arr2.append(nums2[i])

        return [arr1, arr2]
        