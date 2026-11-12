class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for a, num in enumerate(nums):
            # if num is positive three condition will not be reach so break
            if num > 0:
                break

            # check if anchor as duplicate
            if a > 0 and num == nums[a - 1]:
                continue
            
            # Two pointer
            left = a + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([
                        num,
                        nums[left],
                        nums[right]
                    ])

                    # incre/dec right & left
                    left += 1
                    right -= 1

                    # check duple in left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res