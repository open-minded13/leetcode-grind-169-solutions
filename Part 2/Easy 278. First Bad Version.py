# Date of Last Practice: Oct 29, 2023 -> Feb 2, 2024
#
# Time Complexity: O(log N), where N is the amount of all versions.
#                            In each step of the binary search, we reduce the search space by half.
#                            Therefore, it takes logarithmic time to find the first bad version.
#
# Space Complexity: O(1). The solution uses a constant amount of space to store variables,
#                         regardless of the input size. It does not use any data structures that depend on the input size.


def isBadVersion(version):
    # Replace this with your actual isBadVersion implementation
    return version >= 4


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_bound = 1
        right_bound = n
        while left_bound <= right_bound:
            if left_bound == right_bound:
                return left_bound
            version_to_check = (left_bound + right_bound) // 2
            if isBadVersion(version_to_check):
                right_bound = version_to_check
            else:
                left_bound = version_to_check + 1


# Test cases
solution = Solution()

# Test case 1: n = 5, first bad version is 4
print(solution.firstBadVersion(5))  # Output should be 4

# Test case 2: n = 10, first bad version is 4
print(solution.firstBadVersion(10))  # Output should be 4

# Test case 3: n = 1, only one version which is bad
print(solution.firstBadVersion(1))  # Output should be 1
