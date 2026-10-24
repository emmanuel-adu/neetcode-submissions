class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [2,-3,4,-2,2,1,-1,4]
        # Reset → Add → Max
        maxSub = float("-inf")
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
        