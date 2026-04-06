class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for n in nums:
            length = 1
            while (n+1) in setNums:
                length += 1
                longest = max(longest, length)
                n += 1
                if (n+1) not in setNums:
                    length = 1
                    break
            longest = max(longest, length)
        return longest

