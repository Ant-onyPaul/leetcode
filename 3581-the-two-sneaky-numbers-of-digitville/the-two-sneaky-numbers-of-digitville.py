class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                arr.append(nums[i])
            else:
                seen.add(nums[i])
        return arr
