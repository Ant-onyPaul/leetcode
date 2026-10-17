# 
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []

        for i in range(len(nums)):
            digitsum = sum(map(int, str(nums[i])))
            arr.append((digitsum, nums[i]))

        arr.sort()

        arr1 = []
        for item in arr:
            arr1.append(item[1])

        # Store each number's current index
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i

        count = 0

        for i in range(len(nums)):
            if nums[i] != arr1[i]:

                j = pos[arr1[i]]

                # Update positions before swapping
                pos[nums[i]] = j
                pos[nums[j]] = i

                nums[i], nums[j] = nums[j], nums[i]
                count += 1

        return count