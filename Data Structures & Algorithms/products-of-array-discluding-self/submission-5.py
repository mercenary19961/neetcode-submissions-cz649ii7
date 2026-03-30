class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sum_n = 1
        zero = 0
        for n in nums:
            if n != 0:
                sum_n = sum_n * n # 48
            else:
                zero += 1
            
        for i in range(len(nums)):
            if zero == 0:
                res[i] = sum_n // nums[i] # 48 // 1 = 48
            elif zero == 1:
                if nums[i] == 0:
                    res[i] = sum_n
                else:
                    res[i] = 0
            else:
                res[i] = 0
        return res

                

        