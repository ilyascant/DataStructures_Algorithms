class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        # append() 0, so we calculate what is left in stack
        heights.append(0)

        for i,h in enumerate(heights):
            # We keep last index, because right side can extend to left if it is less
            # for exp: 5,6,2,3,5,0 -> if we do not last index it can extend right but not left
            # but after we pop() 5, we keep its index so we can extend to left
            last_i = i
            while stack and stack[-1][-1] > h:
                last_i, last_h = stack.pop()
                maxArea = max(maxArea, (i - last_i) * last_h)

            stack.append((last_i,h))
        
        return maxArea