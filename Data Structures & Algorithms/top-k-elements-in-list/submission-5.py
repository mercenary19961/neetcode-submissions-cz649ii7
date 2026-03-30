class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        arr = []
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for n in range(k):
            maxV = 0
            maxK = 0
            for key in hashmap:
                if hashmap[key] > maxV:
                    maxV = hashmap[key]
                    maxK = key
            arr.append(maxK)
            del hashmap[maxK]
        return arr