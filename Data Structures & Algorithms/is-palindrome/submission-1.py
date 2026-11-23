class Solution:
    def isPalindrome(self, s: str) -> bool:             # checks if string is a palindrome, ignoring non-alphanumeric chars and case
        result = ""
        for c in s:
            if c.isalnum():
                result = result + c.lower()
        return result == result[::-1]