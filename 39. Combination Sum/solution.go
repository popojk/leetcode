package main

// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.

// You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times.

// Two combinations are unique if the frequency of at least one of the chosen numbers is different.

// The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

// hint: 因為每個子集不用考慮順序，每次backtrack i由start開始才能確保每個start重復使用都會在前面例如[2, 2, 3]，不會發生[2, 3, 2]這種錯誤情況

func backTrack(currentSum, target int, start int, path []int, res *[][]int, candidates []int) {
    if currentSum > target {
        return
    }
    if currentSum == target {
        pathCopy := make([]int, len(path))
        copy(pathCopy, path)
        *res = append(*res, pathCopy)
        return
    }
    for i := start; i < len(candidates); i++ {
        path = append(path, candidates[i])
        // 傳入 i（而不是 i+1），因為允許重複使用當前數字
        backTrack(currentSum+candidates[i], target, i, path, res, candidates)
        path = path[:len(path)-1]
    }
}

func combinationSum(candidates []int, target int) [][]int {
    res := [][]int{}
    backTrack(0, target, 0, []int{}, &res, candidates)
    return res
}