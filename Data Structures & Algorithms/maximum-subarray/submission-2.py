class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurr = maxVal = nums[0]

        for i in range(1, len(nums)):
            maxCurr = max(nums[i], maxCurr + nums[i])
            maxVal = max(maxVal, maxCurr)

        return maxVal