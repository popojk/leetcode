
def max_score(input):
    dp = [0] * len(input)
    for i in range(1, len(input)):
        for j in range(i):
            dp[i] = max(dp[j]+(input[i]*(i-j)), dp[i])
    return dp[-1]


# Test cases
test_cases = [
    [1, 2, 3, 4, 5],  # Example test case
    [5, 4, 3, 2, 1],  # Reverse order
    [2, 4, 6, 8, 10],  # Even numbers
    [3, 5, 2, 8, 1],  # Random order
    [1, 1, 1, 1, 1],  # All equal
    [5, 3, 5, 3, 5]   # Alternating
]

# Run test cases
for i, stones in enumerate(test_cases):
    max_total_score = max_score(stones)
    print(f"Test case {
          i+1}: Stones = {stones}, Maximum total score = {max_total_score}")
