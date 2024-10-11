1. **Buttom up DP**

- bottom up遍歷到target前的每個值，每次遍歷值-nums的任一num，如果大於零且這個值有到訪過，代表dp[i]可以被湊成，將dp[i]+=dp[i-num]
- base case: target 0肯定能到達，起始點設為[1, True]，從target 1開始遍歷，假設第一個num是1，dp[i] += dp[1-1]
- *時間複雜度O(Target * N)，空間複雜度O(Target)*