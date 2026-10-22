class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return an array output where each index is the product the array besides it's self
        # Prefix -> Suffix -> Product
        # get the length of nums
        n = len(nums)

        # create length sized array with value 1
        product_list = [1] * n

        # Prefix (left to right)
        prefix = 1
        for i in range(n):
            product_list[i] = prefix
            prefix *= nums[i]
        
        # suffix (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            product_list[i] *= suffix # multiple prefix * suffix
            suffix *= nums[i]
        
        return product_list

        