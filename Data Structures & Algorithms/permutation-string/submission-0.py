class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1) # {a:1, b:1, c:1}
        window = Counter(s2[:len(s1)]) # {l:1, e:1, c:1}

        if s1Count == window:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            left = s2[r - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == s1Count:
                return True

        return False
