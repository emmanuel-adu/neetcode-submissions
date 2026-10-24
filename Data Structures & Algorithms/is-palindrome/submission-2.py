class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the input
        clean = [char.casefold() for char in s if char.isalnum()]

        # Two pointer
        # i tracks prefix
        # j tracks suffix
        i = 0
        j = len(clean) - 1

        while i < j:
            if clean[i] != clean[j]:
                return False
            
            i += 1
            j -= 1
        return True
