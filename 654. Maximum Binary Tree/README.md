1. **recursive, devide and conquer：**

- 查找陣列最大值和其索引，使用找到的最大值創建一個新的樹節點
- 如果最大值左邊還有元素（max_idx > 0），遞迴調用當前函數，以最大值左側的子陣列作為新的輸入陣列，構建當前節點的左子樹
- 如果最大值右邊還有元素（len(nums) - 1 > max_idx），遞迴調用當前函數，以最大值右側的子陣列作為新的輸入陣列，構建當前節點的右子樹
- 返回創建的節點作為子樹的根節點或整棵樹的根節點
- *時間複雜度O(N ** 2)，空間複雜度O(N)*

2. **Stack：**
- 建造一個stack nodes，for loop遍歷nums
- 如果num大於nodes最上面的節點，代表num就是目前左側最大子節點，用while loop測驗這個條件，條件成立就pop 並放到num左側，直到條件不成立
- 經過上述如果nodes還有節點，代表那就是第一個大於num的節點，那就直接把num放入nodes中最上層節點右側，只要符合降冪排序就會一直放入
- 把node放入nodes
- *時間複雜度O(N)，空間複雜度O(N)*