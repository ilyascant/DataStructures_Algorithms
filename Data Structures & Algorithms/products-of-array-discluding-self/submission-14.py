class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]  

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1

        for num in nums:
            if not num:
                zero_count += 1
            else:
                total *= num

        res = []
        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if not num:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)

        return res
