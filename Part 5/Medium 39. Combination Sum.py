from typing import List

# Date of Last Practice: Dec 22, 2023
#
# Time Complexity: O(N * 2^T), where N is the number of candidates and
#                  T is the number of the target variable.
#
# 1. Iterating Over Candidates (O(N)): We start by iterating over each of the
#    N candidates. This step forms the outer loop of our algorithm and contributes
#    an O(N) factor to the overall complexity.
#
# 2. Backtracking Recursion (O(2^T)): Within this loop, for each candidate,
#    we initiate a backtracking process. This can be visualized as traversing a decision tree,
#    where each node represents a decision (to choose or not to choose) for that candidate.
#    The depth of this tree accounts for the number of times a candidate is chosen.
#    The process continues until the cumulative sum of the chosen numbers meets or
#    exceeds our target sum T. In the worst case, this leads to an exponential growth
#    in the number of recursive calls, approximating O(2^T) in complexity.
#
# 3. Overall Complexity (O(N * 2^T)): By combining these two aspects,
#    since the backtracking recursion occurs for each candidate,
#    the overall time complexity in the worst case is O(N * 2^T).
#    This is a theoretical upper bound that reflects the full scope of
#    exploring all possible combinations.
#
# 4. Practical Considerations: It's important to note, however,
#    that this theoretical upper bound is often not reached in practice.
#    The algorithm benefits from early termination in the recursion,
#    where paths that exceed the target sum T are quickly abandoned,
#    thus reducing the actual number of recursive calls.
#
# Note: The term "backtracking" in the context of algorithms refers to
#       a method where the algorithm explores potential solutions to a problem
#       and "backtracks" to try different solutions if the current path doesn't
#       lead to a successful outcome. It's like going down a path,
#       realizing it's not leading to the desired destination,
#       and then stepping back to try a different path. Depth-First Search (DFS) is
#       often closely associated with the backtracking method.
#
# Space Complexity: O(T), where T is the number of the target variable.
#                   The space complexity is O(T), mainly due to the recursion stack depth,
#                   which could be as deep as the target value in the worst case.
#                   Additionally, space is needed to store the combinations,
#                   but this does not impact the worst-case space complexity.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination, total):
            if total == target:
                results.append(list(combination))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()

        results = []
        backtrack(0, [], 0)
        return results


class DP_Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for candidate in candidates:
            for i in range(candidate, target + 1):
                if i == candidate:
                    dp[i].append([candidate])
                if dp[i - candidate]:
                    for item in dp[i - candidate]:
                        # If you use "new_combination = item",
                        # you will also modify "item" since it is a list.
                        # Remember to use the copy() function.
                        new_combination = item.copy()
                        new_combination.append(candidate)
                        dp[i].append(new_combination)
                print(f"dp[{i}]: {dp[i]}")

        return dp[target]


# Test cases
sol = DP_Solution()

# Test case 0
candidates0 = [2, 3]
target0 = 10
print(
    f"Test case 0: {sol.combinationSum(candidates0, target0)}"
)  # Expected: [[2,2,2,2,2],[2,2,3,3]]

# Test case 1
candidates1 = [2, 3, 6, 7]
target1 = 7
print(
    f"Test case 1: {sol.combinationSum(candidates1, target1)}"
)  # Expected: [[2,2,3],[7]]

# # Test case 2
candidates2 = [2, 3, 5]
target2 = 8
print(
    f"Test case 2: {sol.combinationSum(candidates2, target2)}"
)  # Expected: [[2,2,2,2],[2,3,3],[3,5]]

# # Test case 3
candidates3 = [2]
target3 = 1
print(f"Test case 3: {sol.combinationSum(candidates3, target3)}")  # Expected: []
