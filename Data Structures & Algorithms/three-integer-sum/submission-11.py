class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if i != 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                total = sortedNums[i] + sortedNums[l] + sortedNums[r]
                if l < r and total > 0:
                    r -= 1
                elif l < r and total < 0:
                    l += 1
                else:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1
                    while l < r and sortedNums[l] == sortedNums[l-1]:
                        l += 1
        return res
                