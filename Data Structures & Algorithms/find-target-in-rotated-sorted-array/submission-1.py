class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: # nums = [3,4,5,6,1,2], target = 1
            m = (l + r) // 2  # m = 2  |  nums[m] = 5
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # 3 < 5 | correct 
                if target > nums[m] or target < nums[l]: # 1 > 5 wrong | 1 < 3 correct
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1 


