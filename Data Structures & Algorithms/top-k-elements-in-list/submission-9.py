from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time complexity = o(nlogn)
        # space complexity = o(n)
        # get count o(n)
        count = Counter(nums)

        # sort by freq: o(nlogn) 
        sort = sorted(count.items(), key=lambda x:x[1], reverse=True)[:k]
        return [k for k,v in sort]