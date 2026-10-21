from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most frequent elements within the array

        # method one
        # 1. count frequency of each element in list
        num_freq = Counter(nums)
        # 2. sort count by frequency and slice to k
        sorted_num = sorted(num_freq.items(), key=lambda x:x[1], reverse=True)[:k]
        print(sorted_num)
        # 3. return keys
        return [num for num, freq in sorted_num]
        