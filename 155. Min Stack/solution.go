package main

// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// Implement the MinStack class:

// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// You must implement a solution with O(1) time complexity for each function.

type MinStack struct {
    minQ []int
    maxQ []int
}


func Constructor() MinStack {
    return MinStack{minQ: []int{}, maxQ: []int{},}
}


func (m *MinStack) Push(val int)  {
    
}


func (m *MinStack) Pop()  {
    
}


func (m *MinStack) Top() int {
    
}


func (m *MinStack) GetMin() int {
    
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */