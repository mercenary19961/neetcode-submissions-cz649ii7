class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {} # {"act": ["act"]}
        for s in strs:
            key = ''.join(sorted(s))

            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = []
                hashmap[key].append(s)

        return list(hashmap.values())
        