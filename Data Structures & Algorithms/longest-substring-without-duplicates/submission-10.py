class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"abcabcbb"
        hashmap = {} # {a:0, b:1, c:2}
        l = 0
        res = 0 # 1
        for r in range(len(s)):
            while s[r] in hashmap:
                del hashmap[s[l]]
                l += 1
            hashmap[s[r]] = r
            res = max(res, r - l + 1)
        return res
