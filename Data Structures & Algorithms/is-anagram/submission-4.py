class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS = {}
        hashT = {}

        for c in s:
            hashS[c] = 1 + hashS.get(c, 0)
        
        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)

        for key in hashS:
            if hashS[key] != hashT.get(key, 0):
                return False

        return True