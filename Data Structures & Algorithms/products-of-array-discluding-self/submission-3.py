class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        len_ = len(nums)
        for i in range(len_):
            inter = 1
            for j in range(len_):
                if i != j:
                    inter *= nums[j]
            res.append(inter)
        return res