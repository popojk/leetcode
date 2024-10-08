1. **DP**

- bottom up，先求出sum s，每個dp紀錄s中到這個數字能不能被數列中的數字湊成
- 遍歷nums，每輪遍歷確認從s 到num的curr是不是有在dp出現過，或者curr-num有出現過，就代表這個數字是可以被湊到的
- 但就是確認dp[s//2]是不是True
- *時間複雜度O(N * S)，空間複雜度O(S)*