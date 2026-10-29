import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a palindrome reads the same forward/backward
        # case insentive/ ignores all non-aphanumeric characters
        
        # clean the input
        clean_s = "".join(re.findall("[a-zA-Z0-9]+", s)).casefold()
        # s="Was it a car or a cat I saw?" -> WasitacaroracatIsaw

        # two pointer approach
        # i = front
        # j = back
        i = 0
        j = len(clean_s) - 1
        while i < j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
        return True
        