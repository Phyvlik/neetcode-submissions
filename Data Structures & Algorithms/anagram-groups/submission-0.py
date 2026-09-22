class Solution:                                                    # defines the solution class
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # takes list of strings, returns grouped anagrams
        res = defaultdict(list)                                    # dict that auto-creates an empty list for new keys
        for s in strs:                                              # loop through each string in the input
            sortedS = ''.join(sorted(s))                            # sort letters, rejoin into string (anagram fingerprint)
            res[sortedS].append(s)                                   # group original string under its fingerprint
        return list(res.values())                                    # return the grouped lists, without the keys