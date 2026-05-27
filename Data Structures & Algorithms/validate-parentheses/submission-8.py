class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]": "[", "}": "{", ")": "(" }
        stack = []
        for c in s:
            if c in hashmap and stack:
                if hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False