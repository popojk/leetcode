"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""

# the mission is to check whether enough ( provided for ) to close
# every time * shown, we can treat it as ) or (
# if treat as ), left_min -= 1
# if treat as (, left_max += 1

# if in the end left_min == 0, it means the answer is valid
# if left_max < 0, it means not valid

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Time: O(N)
        Space: O(1)
        """
        left_min, left_max = 0, 0
        for c in s:
            if c == '(':
                left_min, left_max = left_min+1, left_max+1
            elif c == ')':
                left_min, left_max = left_min-1, left_max-1
            else:
                left_min, left_max = left_min-1, left_max+1
            
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0