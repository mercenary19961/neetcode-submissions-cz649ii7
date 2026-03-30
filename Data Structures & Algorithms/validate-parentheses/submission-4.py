class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in range(len(s)): # (
            if stack and s[i] in hashmap:
                if hashmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False


