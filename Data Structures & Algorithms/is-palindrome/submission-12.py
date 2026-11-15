import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean input
        clean = "".join(re.findall("[a-zA-Z0-9]+", s)).casefold()
        print(clean)
        # two poitner
        i = 0
        j = len(clean) - 1

        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        
        return True

        