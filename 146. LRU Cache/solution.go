package main

type Node struct {
	Prev, Next *Node
	Key, Value int
}

type LRUCache struct {
    Mp map[int]*Node
	Capacity int
	Head *Node
	Tail *Node
}

func newNode(key, value int) *Node {
	return &Node {
		Key: key,
		Value: value,
	}
}

func newLRUCache(head, tail *Node, capacity int) LRUCache {
	return LRUCache{
		Mp: make(map[int]*Node),
		Capacity: capacity,
		Head: head,
		Tail: tail,
	}
}


func Constructor(capacity int) LRUCache {
    head, tail := newNode(0, 0), newNode(0, 0)
	head.Next = tail
	tail.Prev = head
	return newLRUCache(head, tail, capacity)
}


func (this *LRUCache) Get(key int) int {
	if node, ok := this.Mp[key]; ok {
		// remove original node
		this.remove(node)
		// insert original node to front
		this.insert(node)
		// return value
		return node.Value
	}
	return -1
}


func (this *LRUCache) Put(key int, value int)  {
	// if key existed in Mp, remove org node first
	if node, ok := this.Mp[key]; ok {
		this.remove(node)
	}
    // if Mp len == capacity, remove tail node first
	if len(this.Mp) == this.Capacity {
		this.remove(this.Tail.Prev)
	}
	// insert node
	this.insert(newNode(key, value))

}

func (this *LRUCache) remove(node *Node) {
	delete(this.Mp, node.Key)
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
}

func (this *LRUCache) insert(node *Node) {
	this.Mp[node.Key] = node
	next := this.Head.Next
	this.Head.Next = node
	node.Prev = this.Head
	node.Next = next
	next.Prev = node
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */