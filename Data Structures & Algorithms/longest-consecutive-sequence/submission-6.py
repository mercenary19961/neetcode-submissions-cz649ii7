class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        hashmap = {}
        largest = 0
        current = 0
        for n in nums:
            if n - 1 not in set_nums:
                current = 0

            current += 1
            while n + current in set_nums:
                current += 1
            largest = max(largest, current)
            current = 0
        return largest
