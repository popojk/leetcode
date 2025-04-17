package main

import "container/heap"

type MinHeap []int

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(a, b int) bool { return h[a] < h[b] }
func (h MinHeap) Swap(a, b int) { h[a], h[b] = h[b], h[a] }

func (h *MinHeap) Push(val interface{}) {
	*h = append(*h, val.(int))
}

func (h *MinHeap) Pop() interface{} {
	n := len(*h)
	val := (*h)[n-1]
	*h = (*h)[:n-1]
	return val
}



type KthLargest struct {
    MinHeap *MinHeap
	K int
}


func Constructor(k int, nums []int) KthLargest {
	h := &MinHeap{}
	heap.Init(h)
	kl := KthLargest{MinHeap: h, K: k}
    for _, num := range nums {
		kl.Add(num)
	}
	return kl
}


func (this *KthLargest) Add(val int) int {
    if len(*this.MinHeap) < this.K {
		heap.Push(this.MinHeap, val)
	} else if val > (*this.MinHeap)[0] {
		(*this.MinHeap)[0] = val
		heap.Fix(this.MinHeap, 0)
	}
	return (*this.MinHeap)[0]
}