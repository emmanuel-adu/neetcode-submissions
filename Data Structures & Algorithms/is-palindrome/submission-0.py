class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First strip input string of case, alpha-numeric, whitespaces
        cleaned_s = "".join(char.casefold() for char in s if char.isalnum())

        # Use two pointer approach
        # left pointer increments
        left = 0
        # right pointer increments
        right = len(cleaned_s) - 1

        while left < right:

            # Return False if rhs == lhs
            if cleaned_s[left] != cleaned_s[right]:
                return False
            
            # update pointers
            left += 1
            right -= 1

        return True
        