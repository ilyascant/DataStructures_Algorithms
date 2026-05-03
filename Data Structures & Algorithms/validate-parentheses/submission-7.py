class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 != 0:
            return False

        stack = []
        parentheses = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        for char in s:
            if char in parentheses:
                if stack and parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return len(stack) == 0
