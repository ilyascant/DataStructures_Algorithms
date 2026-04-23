import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for val in strs:
            sortedVal = "".join(sorted(val))
            print(val, sortedVal)
            hash_map[sortedVal].append(val)

        return list(hash_map.values())