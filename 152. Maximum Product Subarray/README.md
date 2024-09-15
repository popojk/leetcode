1. **DP：**

- 對於數組中的每一個元素 n，我們會計算該元素與當前的 curr_max 和 curr_min 乘積，來得到包含此元素的最大和最小乘積
- 計算出 n, n*curr_max 和 n*curr_min 的值，並更新當前的最大值 curr_max 和最小值 curr_min
- curr_max 與 res 進行比較，更新最大結果 res
- *時間複雜度O(N)，空間複雜度O(1)*