class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                count = 0

                while current in nums_set:
                    current += 1
                    count += 1
                
                longest = max(longest, count)
        return longest

        