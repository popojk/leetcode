from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Time: O(N)
        Space: O(N)
        '''
        count = 0
        prefix_sum = 0
        prefix_sum_map = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_map:
                count += prefix_sum_map[prefix_sum-k]
            if prefix_sum in prefix_sum_map:
                prefix_sum_map[prefix_sum] += 1
            else:
                prefix_sum_map[prefix_sum] = 1

        return count