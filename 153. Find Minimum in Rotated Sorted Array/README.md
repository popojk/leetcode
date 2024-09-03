1. **二元搜尋法：**

- 用二元搜尋法查找，如果中點的值大於右指針，代表最小值在右邊，左指針設為中點+1繼續下一循環。
- 反之，最小值在左邊，將右指針設為中點，繼續下一循環。
- 當左右指針相遇，就是最小值所在。
- *時間複雜度O(logN)，空間複雜度O(1)*