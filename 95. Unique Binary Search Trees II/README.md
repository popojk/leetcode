1. **DP：**

- 使用字典 memo 來儲存每對 (start, end) 的生成樹結果，這樣可以避免重複計算。
- 定義函數 generate_trees(start, end) 來生成所有以 start 到 end 為節點的二叉搜索樹。
- 如果 start 大於 end，意味著沒有節點可用，應該返回包含一個 None 的列表，表示樹的這部分是空的。
- 遍歷所有可能的根節點值 root_val，對於每個值，遞歸地生成左右子樹。
- 對於每個可能的根節點，結合其可能的左右子樹，創建一個新的樹節點並加入到列表 trees 中。