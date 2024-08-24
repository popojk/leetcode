1. **Priority Queue：**

- 建造一個defaultdict
- for loop遍歷數列，如每次遞迴的數字num-1當作key在defaultdict為空，代表這是一個新的陣列頭，用heap push key[num]: 1
- 如每次遞迴的數字num-1當作key有在defaultdict出現，heap pop dict[num-1]，並將pop出來的數+1，放入dict[num]，這樣就完成計數
- 遍歷defaultdict，如果有數字小於3就return False
- *時間複雜度O(NlogN)，空間複雜度O(N)*