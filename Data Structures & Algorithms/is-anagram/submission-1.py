class Solution:  # defines the solution class
    def isAnagram(self, s: str, t: str) -> bool: # function takes two strings, returns bool
        if len(s) != len(t): # check if lengths differ
            return False  # different lengths means not an anagram

        return sorted(s) == sorted(t) # sort both strings and compare them