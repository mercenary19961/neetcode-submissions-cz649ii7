class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        all_symbols = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in all_symbols:
                if stack and stack[-1] == all_symbols[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
