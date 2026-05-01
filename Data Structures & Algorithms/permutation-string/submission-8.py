class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        count = [0] * 26
        for i in range(n1):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1

        for r in range(n1, n2):
            if all(x==0 for x in count):
                return True
            
            count[ord(s2[r]) - ord('a')] -= 1
            count[ord(s2[r-n1]) - ord('a')] += 1

        return all(x==0 for x in count)