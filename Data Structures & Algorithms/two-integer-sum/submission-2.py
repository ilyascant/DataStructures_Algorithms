class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        res = []

        for idx, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], idx]

            hash_map[num] = idx

        