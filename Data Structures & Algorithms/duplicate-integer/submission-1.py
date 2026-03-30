class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i -1] and i != 0:
                return True
        return False


        