class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        nums_set = set(nums)
        curr_streak = 0

        for num in nums_set:
            # check if it has a left neighbor
            # no means it a start of a sequence
            if (num - 1) not in nums_set:
                curr_streak = 0
                current = num
                while current in nums_set:
                    current += 1
                    curr_streak += 1
            max_streak = max(curr_streak, max_streak )
        return max_streak

















        # if len(nums) == 0:
        #     return 0
        # curr_streak = 1
        # longest_streak = 0
        # dedupe_nums = set(nums)
        # sorted_nums = sorted(dedupe_nums)
        # for i in range(1, len(sorted_nums)):
        #     diff = sorted_nums[i] - sorted_nums[i - 1]
        #     print(diff)
        #     if diff > 1:
        #         curr_streak = 1
        #     curr_streak += 1
        #     longest_streak = max(curr_streak, longest_streak)
        #     print(longest_streak)
        # return longest_streak
        