1. **Stack：**

- 定義一個res list儲存答案，預設都是0，並定義一個stack list
- for loop遍歷數列，如果遇到比stack頂層值大的數，代表溫度比較高，使用while loop把stack中比現值小的都彈出並做計算
- 返回res
- *時間複雜度O(N)，空間複雜度O(N)*