class Solution:                                 # defines the Solution class (standard LeetCode format)
    def hasDuplicate(self, nums: List[int]) -> bool:  # function takes a list of ints, returns True/False
        nums.sort()                             # sort the list so any duplicate values become adjacent to each other
        for i in range(1, len(nums)):           # loop through the list starting at index 1
            if nums[i] == nums[i - 1]:          # compare each number to the one right before it
                return True                      # if they match, a duplicate was found, so return True
        return False                             # if no adjacent matches were found, there are no duplicates