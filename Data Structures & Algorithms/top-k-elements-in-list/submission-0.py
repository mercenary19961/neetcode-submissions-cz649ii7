class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hashmap = {}
        new_arr = []
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for i in range(k):
            highest = 0
            highest_key = 0
            for key in hashmap:
                if hashmap[key] > highest:
                    highest = hashmap[key]
                    highest_key = key
            new_arr.append(highest_key)
            del hashmap[highest_key]
        return new_arr

            