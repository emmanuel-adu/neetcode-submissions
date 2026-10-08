from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # not optimized solution
        counter = Counter(nums) # o(n)
        # sort by freq, then return top k
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)[0:k] # o(n log n) since we need to sorted every element
        # return key
        return [k for k, v in sorted_counter]