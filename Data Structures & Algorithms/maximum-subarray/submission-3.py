class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = float("-inf")

        for val in nums:
            curr = max(curr + val, val)
            best = max(best, curr)
        
        return best
