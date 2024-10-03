1. **Slide window：**

- right往右移時，代表left -> right都是符合的子陣列，每個起點到right都算是一個子陣列，外加right本身，所以count += 1 + (right - left)
- *時間複雜度O(N)，空間複雜度O(1)*