from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        # o(n)
        freq_dict = Counter(nums) 
        # o(n logk) return k most frequent number
        sorted_tuple = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)[0:k]

        # o(n)
        for key, val in sorted_tuple:
            result.append(key)

        return result

        