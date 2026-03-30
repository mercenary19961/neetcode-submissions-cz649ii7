class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '' 
        for c in strs:
            res += str(len(c)) + "#" + c
        return res

    def decode(self, s: str) -> List[str]: # "5#hello5#world"
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1 # j = 1
            length = int(s[i:j]) # s[0:1] > 5
            i = j + 1  # i = 2
            j = length + i # length = 7
            res.append(s[i:j]) # hello
            i = j
        return res