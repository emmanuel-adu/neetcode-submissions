from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        res = 0

        left = 0
        for right in range(len(s)):
            count.update(s[right])

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
            



