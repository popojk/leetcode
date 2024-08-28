1. **Slide window + Hashmap：**

- 建造一個defaultdict用來儲存每種水果的數量，並宣告變數max_num與left紀錄最大數量與左指針
- for loop遍歷數列，idx當作右指針
- 每次遍歷，右指針水果的數量都+1
- 如果defaultdict長度超過2，左指針水果數量-1，如果左指針水果數量歸零則從defaultdict刪除，最後左指針+1
- *時間複雜度O(N)，空間複雜度O(1)*