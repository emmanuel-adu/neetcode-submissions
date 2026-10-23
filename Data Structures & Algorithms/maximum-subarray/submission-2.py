class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initalize maxSubarray to first value in array
        maxSub = nums[0]
        # current sum is 0
        curSum = 0

        # go through each number in nums
        for n in nums:
            # if we have a negative prefix, remove number from sum
            if curSum < 0:
                curSum = 0
            
            # update current sum
            curSum += n
            # update maxSub
            maxSub = max(maxSub, curSum)
        return maxSub