class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # length of longest consecutive sequence of elements
        # nums = [100,4,200,1,3,2] --> 4
        # what determines a sequence?
        # no number before current number is in set then we know sequence is new
        # then increment count 
        # max of count is longest
        longest = 0 
        set_nums = set(nums)
        for num in set_nums:
            # start of sequence
            if num - 1 not in set_nums:
                curr_count = 0
                while num in set_nums:
                    curr_count += 1
                    num += 1
                longest = max(longest, curr_count)
        return longest