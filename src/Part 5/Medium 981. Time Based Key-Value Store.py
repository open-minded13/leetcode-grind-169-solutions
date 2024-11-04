"""Implements a time-based key-value store.

This module defines the TimeMap class, which stores key-value pairs with 
timestamps and allows retrieval of values at specified timestamps, returning 
the most recent value set before or at the given timestamp.
"""

# Date of Last Practice: Dec 28, 2023 -> Nov 4, 2024
#
# Time Complexity: O(log N), where N is the number of timestamps stored for a key.
#                  This is because we perform a binary search in the get() function.
#
# Space Complexity: O(K * N), where K is the number of unique keys and N is the average
#                   number of timestamp-value pairs per key. This is because for each
#                   key, you are storing a dictionary of timestamps and values or a list
#                   of timestamp-value tuples.


class TimeMap:
    """Time-based key-value store allowing retrieval based on timestamp."""

    def __init__(self):
        """Initialize a dictionary to store key and timestamp-value pairs."""
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store a key-value pair with a specific timestamp.

        Args:
            key: The key associated with the value.
            value: The value associated with the key.
            timestamp: The timestamp when the value was set.
        """
        if key not in self.store:
            self.store[key] = []
        # Append the (timestamp, value) tuple
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Retrieve the latest value for the key at or before the timestamp.

        Args:
            key: The key whose value is to be retrieved.
            timestamp: The timestamp at or before which the value is needed.

        Returns:
            The most recent value set before or at the given timestamp.
            Returns an empty string if no such value exists.
        """
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1

        # Perform binary search to find the closest timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # Check if a valid timestamp exists
        return values[right][1] if right >= 0 else ""


def main():
    """Run test cases to verify the functionality of the TimeMap class."""
    time_map = TimeMap()
    time_map.set("love", "high", 10)
    time_map.set("love", "low", 20)

    # Test cases with assertions
    assert time_map.get("love", 5) == ""  # No value before timestamp 5
    assert time_map.get("love", 10) == "high"  # Exact timestamp match
    assert time_map.get("love", 15) == "high"  # Closest previous timestamp
    assert time_map.get("love", 20) == "low"  # Exact timestamp match
    assert time_map.get("love", 25) == "low"  # Closest previous timestamp

    print("All test cases passed!")


if __name__ == "__main__":
    main()
