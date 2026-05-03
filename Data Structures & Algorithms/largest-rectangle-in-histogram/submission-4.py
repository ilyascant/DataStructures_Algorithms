class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            last_i = i
            while stack and stack[-1][-1] > h:
                last_i, last_h = stack.pop()
                maxArea = max(maxArea, (i-last_i) * last_h)

            stack.append((last_i, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea