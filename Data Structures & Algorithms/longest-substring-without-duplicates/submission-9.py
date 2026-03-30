class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"abcacbb"
        longest = 0
        con = 0
        hashset = set()
        l, r = 0, 0
        while r < len(s) :
            while r < len(s) and s[r] not in hashset:
                hashset.add(s[r])
                con += 1
                r += 1
            hashset.remove(s[l])
            l += 1
            longest = max(longest, con)
            con -= 1
        return longest
            
