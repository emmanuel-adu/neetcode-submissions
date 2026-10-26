class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [2,-3,4,-2,2,1,-1,4]
        # 0 + 2 = 2
        # 2 + -3 
        curr_num = 0
        max_num = float("-inf")

        for num in nums:
            if curr_num < 0:
                curr_num = 0
            
            curr_num += num
            max_num = max(curr_num, max_num)
        
        return max_num

        