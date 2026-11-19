class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find length of the longest substring without duplicate characters
        
        # substring is contiguous char
        # so reset if ord(char) - 1 not in s

        # Expand → Remove Duplicates → Max
        seen = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            # What if s[right] is already in seen?
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add s[right] to seen
            seen.add(s[right])

            # Update longest
            window = right - left + 1
            longest = max(window, longest)

        return longest

