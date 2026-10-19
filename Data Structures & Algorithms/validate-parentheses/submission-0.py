class Solution:
    # checks if brackets are properly matched and nested
    def isValid(self, s: str) -> bool:

        # tracks open brackets we're still waiting to close
        stack = []

        # maps each closing bracket to its matching opening bracket
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # go through the string one character at a time
        for c in s:

            # if this character is a closing bracket
            if c in closeToOpen:

                # check if the top of the stack is its matching open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # it matches, remove that open bracket, it's been closed
                    stack.pop()
                else:
                    # either stack is empty, or top doesn't match
                    # wrong bracket or nothing to close, string is invalid
                    return False

            else:
                # character is an opening bracket
                # push it onto the stack, waiting to be closed later
                stack.append(c)

        # valid only if every open bracket got closed (stack empty)
        return True if not stack else False