"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from collections import deque
from typing import List


class Solution:
    OPERANDS = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        # init a stack to store elements
        stack = []

        def operand(a: str, b: str, operator: str) -> str:
            first_element = int(a)
            second_element = int(b)
            if operator == '+':
                return str(first_element + second_element)
            elif operator == '-':
                return str(first_element - second_element)
            elif operator == '*':
                return str(first_element * second_element)
            elif operator == '/':
                return str(int(first_element / second_element))

        # iterate the tokens
        for token in tokens:
            # if token in operands, do operands
            if token in self.OPERANDS:
                second_element = stack.pop()
                first_element = stack.pop()
                result = operand(first_element, second_element, token)
                stack.append(result)
            # else just push token into stack
            else:
                stack.append(token)
        return int(stack[-1])