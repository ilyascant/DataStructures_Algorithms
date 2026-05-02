class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s and not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        res_len = float('inf')
        start, end = -1, -1
        missing = len(t)

        l = 0
        for r, char in enumerate(s):
            if need.get(char, 0) > 0:
                missing -= 1

            need[char] = need.get(char, 0) - 1
            while missing == 0:
                if r-l+1 < res_len:
                    start, end = l, r
                    res_len = r-l+1

                left_char = s[l]
                need[left_char] += 1

                if need[left_char] > 0:
                    missing += 1

                l += 1

        return s[start: end + 1] if res_len != float('inf') else ""

            


        