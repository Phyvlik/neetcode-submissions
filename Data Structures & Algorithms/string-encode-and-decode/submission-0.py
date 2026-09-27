class Solution:
    def encode(self, strs: List[str]) -> str:      # combines list of strings into one string
        if not strs:                                  # handle empty input list
            return ""                                   # nothing to encode, return empty string

        sizes, res = [], []                            # sizes: lengths of each string; res: pieces to join at the end
        for s in strs:                                 # loop through each string
            sizes.append(len(s))                        # record its length

        for sz in sizes:                                # loop through each recorded length
            res.append(str(sz))                          # add the length as a string
            res.append(',')                               # add a comma to separate lengths from each other

        res.append('#')                                 # marks the end of the length list, start of actual strings
        res.extend(strs)                                # add all the original strings themselves
        return ''.join(res)                              # glue everything into one final string

    def decode(self, s: str) -> List[str]:            # splits encoded string back into original list
        if not s:                                        # handle empty input
            return []                                     # nothing to decode

        sizes, res, i = [], [], 0                        # sizes: lengths we'll parse; res: decoded strings; i: position pointer

        while s[i] != '#':                               # keep reading lengths until we hit the '#' marker
            j = i                                          # second pointer to find the next comma
            while s[j] != ',':                             # scan forward until a comma
                j += 1                                      # keep moving
            sizes.append(int(s[i:j]))                       # digits before the comma are one string's length
            i = j + 1                                        # move past the comma, ready for the next length

        i += 1                                            # move past the '#' marker, now at the start of the actual strings

        for sz in sizes:                                  # loop through each length we recorded
            res.append(s[i:i + sz])                        # grab exactly that many characters
            i += sz                                          # move the pointer past this string

        return res                                          # return the list of decoded strings