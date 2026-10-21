import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most frequent elements within the array

        # method two using an minheap
        count = Counter(nums)
        # 1. initialize an empty heap variable
        heap = []
        # 2. iterate thorugh nums
        for num, freq in count.items():
        # 3. push num to heap
            heapq.heappush(heap, (freq, num))

        # 4. if length of heap is greater than k pop from heap: remove smallest
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
        
        