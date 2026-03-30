class Solution:
    def trap(self, height: List[int]) -> int:
        # res, maxL, maxR, indexL, indexR, total = 0, 0, 0, 0, 0, 0
        # l, r = 0, len(height) - 1
        # while l < r:
        #     if height[l] < height[r]:
        #         if height[l] > maxL:
        #             maxL = height[l]
        #             indexL = l
        #         l += 1
        #     elif height[r] < height[l]:
        #         if height[r] > maxR:
        #             maxR = height[r]
        #             indexR = r
        #         r -= 1
        #     else:
        #         if height[l] > maxL:
        #             maxL = height[l]
        #             indexL = l
        #         if height[r] > maxR:
        #             maxR = height[r]
        #             indexR = r
        #         l += 1
        # selected_area = height[indexL: indexR+1]
        # for i in range(len(selected_area)):
        #     total += maxL - height[i]
        # return total
        if len(height) == 0: return 0
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        