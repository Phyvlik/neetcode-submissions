class Solution:
    def isPalindrome(self, s: str) -> bool:             # checks if string is a palindrome, ignoring non-alphanumeric chars and case
        l, r = 0, len(s) - 1                              # l starts at the beginning, r starts at the end

        while l < r:                                      # keep going until the pointers meet or cross
            while l < r and not self.alphaNum(s[l]):      # skip left pointer forward past any non-letter/digit chars
                l += 1
            while r > l and not self.alphaNum(s[r]):      # skip right pointer backward past any non-letter/digit chars
                r -= 1
            if s[l].lower() != s[r].lower():               # compare the two characters, ignoring uppercase/lowercase
                return False                                 # mismatch means it's not a palindrome
            l, r = l + 1, r - 1                            # move both pointers inward and check the next pair

        return True                                          # pointers met without finding a mismatch, it's a palindrome

    def alphaNum(self, c):                                # helper: checks if a character is a letter or digit
        return (ord('A') <= ord(c) <= ord('Z') or          # true if c is an uppercase letter
                ord('a') <= ord(c) <= ord('z') or           # true if c is a lowercase letter
                ord('0') <= ord(c) <= ord('9'))              # true if c is a digit