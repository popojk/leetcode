1. **Greedy：**

- 使用 while 迴圈來模擬跳躍過程，當 far 小於 len(nums) - 1（未到達終點時），重複以下步驟
- 尋找當前範圍內的最遠可跳點：遍歷從 near 到 far 的每一個位置，計算在每個位置的最大跳躍範圍，即 farest = max(farest, i + nums[i])
- 更新 near 和 far：將 near 更新為下一次跳躍的起點，將 far 更新為當前跳躍可以到達的最遠位置，即 farest
- 增加跳躍次數：每次成功跳躍後，jumps 加 1
- *時間複雜度O(N)，空間複雜度O(1)*