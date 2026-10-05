from collections import Counter

# Time complexity is O(n)
# Space complexity is O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_frequency = Counter(nums)
        for key, val in nums_frequency.items():
            if val > 1:
                return True
        return False

        