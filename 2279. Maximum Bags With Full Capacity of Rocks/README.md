1. **Heap：**

- 初始化count用來計算可以完全填滿的背包數量，以及heap空列表，用來實現最小堆結構
- 遍歷 capacity 和 rocks 列表，計算每個背包的剩餘容量（capacity[i] - rocks[i]），並將其推入堆中
- 當 additionalRocks 大於 0 且堆不為空時，從堆中彈出最小的元素（space_left），這表示當前需要最少石頭就能填滿的背包
- 如果 additionalRocks 足夠填滿該背包（space_left），則 count 加 1，並從 additionalRocks 中扣除相應的石頭數量
- 如果不足以填滿該背包，則終止循環
- 函數返回能完全被額外石頭填滿的背包數量 count
- *時間複雜度O(NlogN)，空間複雜度O(N)*

2. **List sort：**
- 使用列表推導式結合 zip 函數遍歷 capacity 和 rocks 兩個列表，計算出每個背包的剩餘容量（cap - rock），結果存儲在列表 space_left 中
- 將 space_left 列表進行排序。這樣可以確保我們先處理需要較少石頭就能填滿的背包，這樣做可以最大化使用額外的石頭
- 初始化一個計數器 count 為 0，用來記錄可以完全填滿的背包數量
- 遍歷排序後的 space_left，對於每個剩餘空間，如果 additionalRocks （額外的石頭數）大於或等於當前背包的剩餘空間，則增加 count，並從 additionalRocks 中扣除相應的石頭數量，如果 additionalRocks 不足以填滿當前背包，則跳出循環
- 函數返回能完全被額外石頭填滿的背包數量 count
- *時間複雜度O(NlogN)，空間複雜度O(N)*
- 雖然時間複雜度相同但是執行logN操作的次數較最小堆積算法來得小，所以執行效能較高