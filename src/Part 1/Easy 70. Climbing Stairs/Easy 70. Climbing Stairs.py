# Date of Last Practice: Oct 28, 2023 -> Feb 1, 2024
#
# Time Complexity: O(N), where N is the number of steps we have on the stair.
#                  This is because we use a for loop to iterate from 3 to N.
# Space Complexity: O(1) because we use a constant amount of extra space to store three variables.


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        valid_ways_when_i_minus_2 = 1
        valid_ways_when_i_minus_1 = 2
        valid_ways_when_i = 0
        for _ in range(3, n + 1):
            valid_ways_when_i = valid_ways_when_i_minus_1 + valid_ways_when_i_minus_2
            valid_ways_when_i_minus_2 = valid_ways_when_i_minus_1
            valid_ways_when_i_minus_1 = valid_ways_when_i
        return valid_ways_when_i


class Ineffective_Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(2^N), where N is the number of steps we have on the stair.
        #                  This is because we use depth-first search to explore all possible paths,
        #                  making it exponential in time complexity.
        #                  Though the base number is not exactly 2 (e.g., 1.7, 1.8, etc.),
        #                  we can still say it is O(2^N).
        # English Classroom:
        # -> "2^N" is "two raised to the power of N."
        # -> "2" is the base number, and "N" is the exponent.
        valid_ways = 0
        stack = []
        stack.append(0)
        while stack:
            step_counter = stack.pop()
            if step_counter == n:
                valid_ways += 1
            elif step_counter > n:
                continue
            else:
                stack.append(step_counter + 1)
                stack.append(step_counter + 2)
        return valid_ways


# Test cases
solution = Solution()
print(solution.climbStairs(1))  # Should print 1
print(solution.climbStairs(2))  # Should print 2
print(solution.climbStairs(3))  # Should print 3
print(solution.climbStairs(4))  # Should print 5
print(solution.climbStairs(5))  # Should print 8
