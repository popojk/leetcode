1. **DP**

- bottom up, 每個dp可以是當前值加上先前的最大，或者僅當前值，取最大者放入dp
- 如當前dp比max_sum大，更新max_sum
- *時間複雜度O(N)，空間複雜度O(1)*