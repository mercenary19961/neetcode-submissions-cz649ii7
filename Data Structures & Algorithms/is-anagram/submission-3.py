class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        hashmapT = {}
        hashmapS = {}
        for i in range(len(t)):
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        for key in hashmapT:
            if hashmapT[key] != hashmapS.get(key, 0):
                return False
        return True