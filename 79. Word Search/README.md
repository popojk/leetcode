1. **recursive+backtracking**

- 創建 search函式，傳入chars(剩餘的字串),row, col, set(紀錄走訪過的)
- basecase: chars第一個字與走訪節點不同，反之chars長度剩1返回True
- 其他狀況下，將row, col存入set紀錄已走訪過，並向四個方向遞迴，如果該方向已走訪過則不走
- 將row, col從set移除，完成backtracking
- *時間複雜度O(M * N * 4 ^ l)，空間複雜度O(l)，l代表字串長度*