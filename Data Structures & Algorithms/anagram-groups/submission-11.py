import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for val in strs:
            count = [0] * 26
            for char in val:
                count[ord(char) - ord('a')] += 1
            hash_map[tuple(count)].append(val)

        return list(hash_map.values())


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for val in strs:
            sortedVal = "".join(sorted(val))
            hash_map[sortedVal].append(val)

        return list(hash_map.values())