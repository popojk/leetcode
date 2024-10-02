1. **BFS：**

- 在二元樹中計算節點的index，當前節點index等於2*parent index+1
- 用BFS計算每層最右與最左index差異，並取最大值
- *時間複雜度O(N)，空間複雜度O(N)*