"""
Check if a matrix is a Toeplitz matrix.

This module defines a class `Solution` with methods to verify if a given matrix
is a Toeplitz matrix, where every diagonal from top-left to bottom-right has the 
same elements. It includes solutions for scenarios with limited memory constraints.

Typical usage example:

    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    solution = Solution()
    assert solution.isToeplitzMatrix(matrix) is True
    assert solution.isToeplitzMatrixMemoryLimited(matrix) is True
"""

from typing import List, Iterator

# Date of Last Practice: Sep 24, 2024
#
# Time Complexity: O(M*N), where M is the number of rows and N is the number of columns.
#                  We iterate over all elements of the matrix.
#
# Space Complexity: O(1), as we are not using any additional data structures.


class Solution:
    """Checks if a matrix is a Toeplitz matrix."""

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Returns whether a matrix is a Toeplitz matrix.

        Args:
            matrix: A list of lists of integers representing the matrix.

        Returns:
            bool: True if the matrix is Toeplitz, otherwise False.
        """
        # Step 1 - Iterate over the matrix starting from second row and column.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # Step 2 - Check if the current element is equal to the element
                #          diagonally above.
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    # Step 3 - Return False if any element does not match.
                    return False
        # Step 4 - Return True if all diagonals have the same elements.
        return True

    def isToeplitzMatrixDiskLimited(self, matrix_iterator: Iterator[List[int]]) -> bool:
        """
        Checks if a matrix is Toeplitz with limited memory, loading one row at a time.

        Args:
            matrix_iterator: An iterator that yields one row of the matrix at a time.

        Returns:
            bool: True if the matrix is Toeplitz, otherwise False.
        """
        # Step 1 - Initialize previous row as None.
        previous_row = None

        # Step 2 - Iterate through each row using the iterator.
        for current_row in matrix_iterator:
            if previous_row is not None:
                # Step 3 - Compare elements with the previous row.
                for j in range(1, len(current_row)):
                    if current_row[j] != previous_row[j - 1]:
                        # Step 4 - Return False if any mismatch is found.
                        return False
            # Step 5 - Update previous row to current row for next iteration.
            previous_row = current_row

        # Step 6 - Return True if all diagonals match.
        return True


def main():
    """
    Demonstrate the usage of the Solution class.
    """
    solution = Solution()

    # Test case 1: Standard Toeplitz matrix
    matrix1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    assert solution.isToeplitzMatrix(matrix1) is True

    # Test case 2: Not a Toeplitz matrix
    matrix2 = [[1, 2], [2, 2]]
    assert solution.isToeplitzMatrix(matrix2) is False

    # Test case 3: Single element matrix
    matrix3 = [[1]]
    assert solution.isToeplitzMatrix(matrix3) is True

    # Test case 4: 2x2 Toeplitz matrix
    matrix4 = [[1, 2], [3, 1]]
    assert solution.isToeplitzMatrix(matrix4) is True

    # Test case 5: 3x3 matrix with different diagonals
    matrix5 = [[1, 2, 3], [4, 1, 2], [5, 4, 1]]
    assert solution.isToeplitzMatrix(matrix5) is True

    # Test case 6: 3x3 matrix with one diagonal different
    matrix6 = [[1, 2, 3], [4, 1, 2], [5, 4, 0]]
    assert solution.isToeplitzMatrix(matrix6) is False

    # Test cases for isToeplitzMatrixDiskLimited
    # Helper generator to simulate loading one row at a time
    def matrix_generator(matrix):
        for row in matrix:
            yield row

    # Test case 7: Standard Toeplitz matrix with disk limited memory
    assert solution.isToeplitzMatrixDiskLimited(matrix_generator(matrix1)) is True

    # Test case 8: Not a Toeplitz matrix with disk limited memory
    assert solution.isToeplitzMatrixDiskLimited(matrix_generator(matrix2)) is False

    # Test case 9: Single element matrix with disk limited memory
    assert solution.isToeplitzMatrixDiskLimited(matrix_generator(matrix3)) is True

    # Test case 10: 2x2 Toeplitz matrix with disk limited memory
    assert solution.isToeplitzMatrixDiskLimited(matrix_generator(matrix4)) is True

    # Output to confirm all tests pass.
    print("All test cases passed.")


if __name__ == "__main__":
    main()
