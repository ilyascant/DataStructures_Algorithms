class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = sorted(count.items(), key=lambda x: x[1])

        res = []
        while len(res) < k:
            res.append(arr.pop()[0])

        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res

