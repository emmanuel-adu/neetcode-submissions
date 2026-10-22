class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n 

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix # Store product BEFORE current number
            prefix *= nums[i]  # Include current number for NEXT index

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix # multiply each position by the product of everything to its right
            suffix *= nums[i]
        
        return output



        