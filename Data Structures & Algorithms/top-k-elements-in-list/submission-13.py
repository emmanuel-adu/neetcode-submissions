from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can create a more optimum solution by using a heap
        # get the freq of each num
        count = Counter(nums)

        # use a heap
        heap = []
        for num, freq in count.items():
            # we will push (freq, num) into heap
            heapq.heappush(heap, (freq, num))

            # if size of heap is larger than k 
            # we pop (freq, num) from heap
            if len(heap) > k:
                heapq.heappop(heap)

        return [v for k, v in heap]