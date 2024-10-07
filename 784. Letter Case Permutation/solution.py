from typing import List


class TopDownSolution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def back_track(remain_str, new_str, res):
            if remain_str == '':
                res.append(new_str)
                return
            if remain_str[0].isalpha():
                chars = [remain_str[0].lower(), remain_str[0].upper()]
                for c in chars:
                    back_track(remain_str[1:], new_str+c, res)
            else:
                back_track(remain_str[1:], new_str+remain_str[0], res)
        back_track(s, '', res)
        return res
