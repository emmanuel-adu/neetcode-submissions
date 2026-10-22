class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       # array of nums
       # return length of longest consequtive sequence of elements

       # Track longest sequence
       longest = 0

       # membership check nums = {2,20,4,10,3,4,5}
       num_set = set(nums)

       # Iterate through nums
       for num in num_set:
        # Check when it's a new sequence
        if (num - 1) not in num_set:
            current = num # 2
            seq_count = 1

            # increment seq count if num + 1 is in set
            while (current + 1) in num_set:
                current += 1
                seq_count += 1
            
            # update longest
            longest = max(longest, seq_count)
            
       return longest

          