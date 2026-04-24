class Solution:
    # Time: O(n), Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

    # Time: O(n), Space: O(n)
    def isPalindrome2(self, s: str) -> bool:
        clean = ''.join(w for w in s if w.isalnum()).lower()

        left, right = 0, len(clean)-1

        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        
        
        return True