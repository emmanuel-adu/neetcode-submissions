from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements with array
        # 1. get counter
        count = Counter(nums)
        # 2. sort by freq
        sorted_nums = sorted(count.items(), key=lambda x:x[1], reverse=True)[:k] # list of tuples
        # 3. return top 2 keys 
        return [k for k,v in sorted_nums]

