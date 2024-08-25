1. **Priority Queue：**

- 建造一個counter dict並計算每個字串出現的次數
- for loop遍歷dict，存入heap list中，次數要加上負號方便heap排序
- heapify排序，出現次數就會由大排到小，因為加上負號，因此最大的會在最上面
- for loop遍歷heap k次，heappop取出最大值
- *時間複雜度O(n + klogn)，空間複雜度O(m)*