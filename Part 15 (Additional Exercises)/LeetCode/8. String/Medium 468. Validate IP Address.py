"""
Validates whether a given string is a valid IPv4 or IPv6 address.

This module contains the Solution class with two methods to validate IP addresses:
1. `validIPAddress`: Original approach using split and validation methods.
2. `validIPAddressRegex`: Optimized approach using regular expressions.
"""

import re

# Date of Last Practice: Sep 24, 2024
#
# Time Complexity: O(N), where N is the length of the input string.
#                  The split method takes O(N), and the validation methods take O(1).
#                  The regex approach also takes O(N) for pattern matching.
#
# Space Complexity: O(N), where N is the length of the input string.
#                   The split method creates a list of chunks with O(N) space.
#                   The regex pattern matching also requires O(N) space for the pattern.
#
#                   Assuming efficient regex matching, the time complexity is O(n).
#                   In practice, due to potential backtracking, the worst-case can
#                   degrade to O(n^2) if the input is designed to exploit regex
#                   weaknesses.


class Solution:
    """Class for IP address validation using multiple approaches."""

    def validIPAddress(self, queryIP: str) -> str:
        """
        Returns the type of IP address for the given query using the split method.

        Args:
            queryIP: A string representing the IP address to be validated.

        Returns:
            str: "IPv4", "IPv6", or "Neither" based on the IP validation.
        """
        # Step 1 - Split the input based on the presence of '.' for IPv4
        ipv4_chunks = queryIP.split(".")

        # Step 2 - Split the input based on the presence of ':' for IPv6
        ipv6_chunks = queryIP.split(":")

        # Step 3 - Validate IPv4 if there are 4 parts
        if len(ipv4_chunks) == 4:
            for chunk in ipv4_chunks:
                if not self._is_ipv4(chunk):
                    return "Neither"
            return "IPv4"

        # Step 4 - Validate IPv6 if there are 8 parts
        if len(ipv6_chunks) == 8:
            for chunk in ipv6_chunks:
                if not self._is_ipv6(chunk):
                    return "Neither"
            return "IPv6"

        # Step 5 - Return "Neither" if not valid for both
        return "Neither"

    def _is_ipv4(self, chunk: str) -> bool:
        """
        Validates a single chunk of an IPv4 address.

        Args:
            chunk: A string representing a part of the IPv4 address.

        Returns:
            bool: True if the chunk is a valid IPv4 part, False otherwise.
        """
        # Check if the chunk is empty or contains non-digit characters
        if not chunk or not chunk.isdigit():
            return False

        # Check for leading zeros in a multi-digit chunk
        if len(chunk) > 1 and chunk[0] == "0":
            return False

        # Check if the chunk is in the valid range of 0 to 255
        return 0 <= int(chunk) <= 255

    def _is_ipv6(self, chunk: str) -> bool:
        """
        Validates a single chunk of an IPv6 address.

        Args:
            chunk: A string representing a part of the IPv6 address.

        Returns:
            bool: True if the chunk is a valid IPv6 part, False otherwise.
        """
        # Check if the chunk is empty or exceeds 4 characters in length
        if not chunk or len(chunk) > 4:
            return False

        # Check if all characters are valid hexadecimal digits
        for char in chunk:
            if not ("0" <= char <= "9" or "a" <= char <= "f" or "A" <= char <= "F"):
                return False

        return True

    def validIPAddressRegex(self, queryIP: str) -> str:
        """
        Returns the type of IP address for the given query using regular expressions.

        Args:
            queryIP: A string representing the IP address to be validated.

        Returns:
            str: "IPv4", "IPv6", or "Neither" based on the IP validation.
        """
        # Improved regex pattern for IPv4 to exclude leading zeros
        ipv4_pattern = re.compile(
            r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$"
        )

        # Regex pattern for IPv6
        ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")

        # Step 1 - Validate against IPv4 pattern
        if ipv4_pattern.findall(queryIP):
            return "IPv4"

        # Step 2 - Validate against IPv6 pattern
        if ipv6_pattern.match(queryIP):
            return "IPv6"

        # Step 3 - Return "Neither" if not matching either pattern
        return "Neither"


# Test cases with assertions to compare both methods
if __name__ == "__main__":
    solution = Solution()

    # Valid IPv4 test case
    assert solution.validIPAddress("172.16.254.1") == "IPv4"
    assert solution.validIPAddressRegex("172.16.254.1") == "IPv4"

    # Valid IPv6 test case
    assert solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert solution.validIPAddressRegex("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"

    # Invalid IP test case
    assert solution.validIPAddress("256.256.256.256") == "Neither"
    assert solution.validIPAddressRegex("256.256.256.256") == "Neither"

    # Invalid IPv4 with leading zero
    assert solution.validIPAddress("192.168.01.1") == "Neither"
    assert solution.validIPAddressRegex("192.168.01.1") == "Neither"

    # Invalid IPv4 with all segments leading zeros
    assert solution.validIPAddress("01.01.01.01") == "Neither"
    assert solution.validIPAddressRegex("01.01.01.01") == "Neither"

    # Invalid IPv6 with incorrect characters
    assert solution.validIPAddress("2001:0db8:85a3::8A2E:037j:7334") == "Neither"
    assert solution.validIPAddressRegex("2001:0db8:85a3::8A2E:037j:7334") == "Neither"

    # Additional test cases for IPv6 with correct and incorrect formats
    assert solution.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert solution.validIPAddressRegex("2001:db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert (
        solution.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == "Neither"
    )
    assert (
        solution.validIPAddressRegex("02001:0db8:85a3:0000:0000:8a2e:0370:7334")
        == "Neither"
    )

    print("All test cases passed for both methods!")
