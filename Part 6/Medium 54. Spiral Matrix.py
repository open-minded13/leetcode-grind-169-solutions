"""
Solution to the "Spiral Matrix" problem.

The Solution class implements two methods to retrieve all elements of a matrix 
in spiral order. The first approach is clean and readable, while the second 
provides an alternative with manual direction control, which can be useful in 
specific scenarios.

Example:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Solution().spiralOrder(matrix)
    print(result)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

from typing import List

# Date of Last Practice: Dec 31, 2023 -> Feb 18, 2024 -> Oct 8, 2024
#
# Time Complexity: O(N * M), where N and M are the number of rows and columns in the
#                  matrix. Given an m * n matrix, each element is visited once.
#
# Space Complexity: O(N * M), where N and M are the number of rows and columns in the
#                   matrix. This is because of the output list. Apart from this,
#                   we only use constant extra space, including top, bottom, left,
#                   and right.


class Solution:
    """Retrieves elements of a matrix in spiral order."""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns a list of matrix elements in spiral order.

        This method uses a clean and structured approach to traverse the matrix
        layer by layer, adjusting the boundaries as it proceeds.

        Args:
            matrix: A list of lists representing the 2D matrix.

        Returns:
            A list containing the matrix elements in spiral order.
        """
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        output = []

        # Step 1 - Traverse the matrix layer by layer, in a spiral pattern
        while left <= right and top <= bottom:
            # Step 2 - Traverse from left to right along the top row
            for col in range(left, right + 1):
                output.append(matrix[top][col])
            top += 1  # Move the top boundary down

            # Step 3 - Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1  # Move the right boundary left

            if left <= right and top <= bottom:
                # Step 4 - Traverse from right to left along the bottom row
                for col in range(right, left - 1, -1):
                    output.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up

                # Step 5 - Traverse from bottom to top along the left column
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1  # Move the left boundary right

        return output

    def spiralOrderManualDirection(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns a list of matrix elements in spiral order using direction control.

        This alternative method uses an approach where directional movement is
        controlled manually by switching between four possible directions: right,
        down, left, and up. It manually updates direction based on whether the matrix
        boundaries have been hit.

        This method is less intuitive and harder to read compared to the structured
        layer-by-layer approach. However, it may be useful when fine-grained control
        over traversal is needed, such as when optimizing for special constraints,
        handling complex matrix shapes, or dealing with dynamic conditions during
        traversal.

        Args:
            matrix: A list of lists representing the 2D matrix.

        Returns:
            A list containing the matrix elements in spiral order.

        When to use:
            - When you need more manual control over the traversal.
            - When you expect more dynamic matrix shapes or want a more flexible
              approach to changing directions.
            - When the spiral order needs more intricate handling beyond simple
              boundaries.
        """
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_direction = 0
        row, col = 0, 0
        output = [matrix[0][0]]

        # Step 1 - Traverse until the boundaries overlap
        while top <= bottom and left <= right:
            # Step 2 - Calculate the direction
            dr, dc = directions[cur_direction]

            # Step 3 - Move in the current direction as long as within bounds
            while top <= row + dr <= bottom and left <= col + dc <= right:
                output.append(matrix[row + dr][col + dc])
                row += dr
                col += dc

            # Step 4 - Adjust boundaries and direction
            if cur_direction == 0:
                top += 1  # Rightward movement, adjust top boundary
            elif cur_direction == 1:
                right -= 1  # Downward movement, adjust right boundary
            elif cur_direction == 2:
                bottom -= 1  # Leftward movement, adjust bottom boundary
            else:
                left += 1  # Upward movement, adjust left boundary

            # Step 5 - Update the direction for the next movement
            cur_direction = (cur_direction + 1) % 4  # Cycle through directions

        return output


def main():
    """
    Main function to demonstrate the usage of both methods in the Solution class.
    """
    # Test cases to validate both methods
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[7], [9], [6]], [7, 9, 6]),
    ]

    # Testing the default method (clean, structured approach)
    solution = Solution()
    for matrix, expected in test_cases:
        assert solution.spiralOrder(matrix) == expected

    # Testing the manual direction method (alternative approach)
    for matrix, expected in test_cases:
        assert solution.spiralOrderManualDirection(matrix) == expected

    print("All test cases passed for both methods!")


if __name__ == "__main__":
    main()
