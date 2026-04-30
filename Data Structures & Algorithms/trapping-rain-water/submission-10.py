class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        leftMax = [0] * len(heights)
        rightMax = [0] * len(heights)

        leftMax[0] = heights[0]
        for i in range(1, len(heights)):
            leftMax[i] = max(leftMax[i-1], heights[i])

        rightMax[len(heights)-1] = heights[len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], heights[i])

        res = 0
        for i in range(len(heights)):
            minWall = min(leftMax[i], rightMax[i])
            res += minWall - heights[i]

        return res