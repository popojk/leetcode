2. **廣度優先搜索（BFS）：**

- 建造一個queue，並輸入根節點(root)
- 建立while loop，queue不為空就繼續
- 每次遞迴先使用size變數紀錄該層級的長度，並使用for loop遞迴這個長度次數已確保一次處理一個層級
- 每次for loop pop出queue第一個Node並賦予變數curr，如果for迴圈的 i不是最後一個idx，curr.next就是queue第一個Node
- 如果curr有left或right，推進queue中
- 以上動作完成後，返回root就是答案
- *時間複雜度O(N)，空間複雜度O(N)*