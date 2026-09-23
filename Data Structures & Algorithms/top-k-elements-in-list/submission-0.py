class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # returns k most frequent elements
        count = {}                                    # dict to store each number's frequency
        for num in nums:                              # loop through every number in the input
            count[num] = 1 + count.get(num, 0)        # increment count, default to 0 if not seen yet

        arr = []                                       # will hold [count, number] pairs
        for num, cnt in count.items():                # loop through each number and its count
            arr.append([cnt, num])                     # store as [count, number] so we can sort by count

        arr.sort()                                     # sort ascending by count (since count is first in each pair)

        res = []                                       # will hold the final answer
        while len(res) < k:                            # keep going until we have k elements
            res.append(arr.pop()[1])                   # pop highest count off the end, grab just the number

        return res                                      # return the k most frequent numbers