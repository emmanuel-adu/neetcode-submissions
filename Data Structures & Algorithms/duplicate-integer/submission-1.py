from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq dict
        freq = Counter(nums)
        for num in nums:
            if freq[num] > 1:
                return True
        # loop thorugh each ele in array
        return False


        