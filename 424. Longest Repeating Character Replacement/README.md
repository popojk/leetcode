1. **Slide window + Hashmap：**

- 建造一個defaultdict用來儲存每種單字的數量，並宣告變數max_len與left紀錄最大長度與左指針，另外宣告max_count來記錄窗口字串最大的字數
- for loop遍歷數列，idx當作右指針
- 每次遍歷，右指針單字的數量都+1，並重新計算窗口字串最大的字數max_count
- 如果窗口長度減去最大字數超過k，代表美辦法完成替換，左指針字數量-1，最後左指針+1
- 回傳max_len就是答案
- 時間複雜度O(N)，空間複雜度O(N)