Given a sequence of stones with non-negative integers, calculate the maximum possible score starting from the beginning to end. You can jump any number of positions from each position. The score is calculated as the destination stone_value * number_of_jump_positions. Essentially the first value in the array doesn't matter as you always jump from beginning and only the destination stone value is considered in the score computation. You need to solve it in less than O(n^2) time.

For example,
Test case 1: Stones = [1, 2, 3, 4, 5], Maximum total score = 20 #you jump to ast position, so the score would be 5 * 4 = 20
Test case 2: Stones = [5, 4, 3, 2, 1], Maximum total score = 10 #you jump one position from beginning to end, so the score would be 4+3+2+1=10
Test case 3: Stones = [2, 4, 6, 8, 10], Maximum total score = 40
Test case 4: Stones = [3, 5, 2, 8, 1], Maximum total score = 25
Test case 5: Stones = [1, 1, 1, 1, 1], Maximum total score = 4
Test case 6: Stones = [5, 3, 5, 3, 5], Maximum total score = 20

1. **DP：**

- 宣告名為dp的一維陣列，長度為input長度，用來儲存跳耀每格的最大值
- 跳到每格i的最佳解，必須要從prefix某j格到i的分數加上j的最佳解得出，j的最佳解可以直接從dp陣列中讀出不需要重複計算
- 用兩個for loop跑完，答案就在dp[-1]
- *時間複雜度O(N^2)，空間複雜度O(N)*

2. **suffix sum：**

- 宣告名為max_suffix的一維陣列，長度為input長度，用來儲存包含該格右邊的最大suffix
- 因為到某格的分數是以步數*石頭數，換句話說找到某格suffix的最大值後，到這個最大值之前的每一步都應填上這個最大值才會是最優解，中間其他值都不用考慮
- 加總max_suffix就會是答案
- *時間複雜度O(N)，空間複雜度O(N)*