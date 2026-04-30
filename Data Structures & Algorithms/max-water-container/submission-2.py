class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxVal = 0

        while left < right:
            diff = right - left
            minVal = min(heights[right], heights[left])
            water = diff * minVal
            maxVal = max(water, maxVal)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxVal
