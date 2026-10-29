class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # Input: nums = [-1,0,1,2,-1,-4]
        # -1 = b + c
        # anchor is i, b and c are twopointer

        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # avoid processing the same anchor twice
            if i > 0 and num == nums[i - 1]:
                continue
            
            # two pointer
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return res
        