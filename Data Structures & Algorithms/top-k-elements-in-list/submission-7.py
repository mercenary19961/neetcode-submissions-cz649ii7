class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # {1:1, 2:2, 3:3}
        res = []

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for i in range(k):
            count_max = 0
            selected_key = 0
            for key in hashmap:
                if hashmap[key] > count_max:
                    selected_key = key
                    count_max = hashmap[key]
                
            res.append(selected_key)
            del(hashmap[selected_key])

        return res

