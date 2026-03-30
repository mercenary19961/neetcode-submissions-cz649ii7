class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # key = sorted_s: value = []
        for s in strs:
            sorted_s = "".join(sorted(s)) # "act"
            if sorted_s not in hashmap:
                hashmap[sorted_s] = [] # {"act": []}
            hashmap[sorted_s].append(s) # {"act": ["act"]}
        return list(hashmap.values())
