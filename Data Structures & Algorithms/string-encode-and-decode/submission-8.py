class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]: # "5#Hello5#World"
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            count = 2
            while s[j] != "#":
                j += 1
                count += 1
            length = int(s[i:j])
            res.append(s[i+count:j+length+1])
            i = j + 1 + length

        return res
