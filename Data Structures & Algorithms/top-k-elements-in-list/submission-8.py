import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)

        for num, freq in counter.items():
            if len(heap) < k:
                # Insert an element and maintain the min-heap property
                # Smallest element is always at heap[0]
                heapq.heappush(heap, (freq, num)) 
            else:
                # Push new element, then remove the smallest
                heapq.heappushpop(heap, (freq, num))
        return [num for freq, num in heap]