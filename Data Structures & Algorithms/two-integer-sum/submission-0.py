class Solution:
    # Takes a list of numbers and a target sum, returns the indices
    # of the two numbers that add up to target
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Loop through each number in the list using its index i
        for i in range(len(nums)):

            # Loop through the numbers that come after i, using index j
            # starting at i+1 so we don't reuse the same number twice
            for j in range(i + 1, len(nums)):

                # Check if this pair of numbers adds up to the target
                if nums[i] + nums[j] == target:

                    # Found the pair, return their indices immediately
                    return [i, j]

        # If no pair was found after checking everything, return empty list
        return []