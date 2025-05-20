"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        # init a normal_stack to store all element and a min_stack to store the minimum element on the top of stack
        self.normal_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # append on normal stack, and append min_stack if val < self.min_stack[-1]
        self.normal_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # slice top of self.normal_stack, and slice min_stack if element.val == self.min_stack[-1]
        top_element = self.normal_stack.pop()
        if top_element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # return self.normal_stack[-1]
        return self.normal_stack[-1]

    def getMin(self) -> int:
        # return self.min_stack[-1]
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
