class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"abcacbb"
        left, right = 0, 0
        highestC = 0
        hashset = set()
        count = 0

        while right != len(s):
            while right != len(s) and s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                count += 1 
            hashset.remove(s[left])
            left += 1         
            highestC = max(highestC, count) 
            count -= 1
        return highestC
