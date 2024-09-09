1. **DP：**

- 題目找出所有pal的組合，可以將思路拆解為，如果左邊preffix是pal，那將這個preffix pal與右側所有的suffix pal組合成一個答案
- 利用快取的方法把每次執行partition的結果儲存在快取
- *時間複雜度O(N * 2^N)，空間複雜度O(N * 2^N)*