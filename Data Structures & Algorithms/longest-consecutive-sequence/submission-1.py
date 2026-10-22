class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list into a set
        numSet = set(nums)

        # initialize longest to track the max length
        longest = 0

        # Iterate numSet
        for num in numSet:
            # check if number is start of sequence
            # this guarantees that consecutive sequence is counted exactly once
            if num - 1 not in numSet:
                current = num
                streak = 1

                # See if num + 1, num + 2 exists in the set and extend streak
                while current + 1 in numSet:
                    current += 1
                    streak += 1

                # Update max streak
                longest = max(longest, streak)
                
        return longest


