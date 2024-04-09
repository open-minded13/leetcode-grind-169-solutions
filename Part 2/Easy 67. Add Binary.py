# Date of Last Practice: Oct 26, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the maximum length of the input strings (a and b).
# Space Complexity: O(N) because the result string grows
#                   in proportion to the maximum length of the input strings (a and b).


class Solution_1:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i, j = len(a) - 1, len(b) - 1
        while i > -1 or j > -1 or carry > 0:
            if i > -1:
                carry += int(a[i])
                i -= 1
            if j > -1:
                carry += int(b[j])
                j -= 1
            result = str(carry % 2) + result
            carry = carry // 2
        return result


class Solution_2:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i, j = len(a) - 1, len(b) - 1
        while i > -1 or j > -1 or carry > 0:
            if i > -1:
                carry += int(a[i])
                i -= 1
            if j > -1:
                carry += int(b[j])
                j -= 1
            result = str(carry % 2) + result
            carry = carry // 2
        return result


# Test cases
if __name__ == "__main__":
    solution1 = Solution_1()
    solution2 = Solution_2()

    # Test Case 1
    a1, b1 = "11", "1"
    print("Test Case 1:")
    print("Expected Output:", "100")
    print("Solution 1 Output:", solution1.addBinary(a1, b1))
    print("Solution 2 Output:", solution2.addBinary(a1, b1))

    # Test Case 2
    a2, b2 = "1010", "1011"
    print("\nTest Case 2:")
    print("Expected Output:", "10101")
    print("Solution 1 Output:", solution1.addBinary(a2, b2))
    print("Solution 2 Output:", solution2.addBinary(a2, b2))

    # Test Case 3
    a3, b3 = "1101", "1011"
    print("\nTest Case 3:")
    print("Expected Output:", "11000")
    print("Solution 1 Output:", solution1.addBinary(a3, b3))
    print("Solution 2 Output:", solution2.addBinary(a3, b3))
