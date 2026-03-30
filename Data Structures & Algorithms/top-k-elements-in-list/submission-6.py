class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        sort_nums = sorted(nums)
        for n in sort_nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for i in range(k):
            max_key = 0
            max_value = 0
            for key in hashmap:
                if hashmap[key] > max_value:
                    max_value = hashmap[key]
                    max_key = key
            res.append(max_key)
            del hashmap[max_key]
        return res