import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the input  
        clean = "".join(re.findall("[A-Za-z0-9]+", s)).casefold()
        print(clean)

        # two pointer approach i tracks start j tracks end
        i = 0
        j = len(clean) - 1
        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        return True
