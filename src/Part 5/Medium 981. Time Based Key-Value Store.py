# Date of Last Practice: Dec 28, 2023
#
# Time Complexity: O(log N), where N is the number of timestamps stored for a key.
#                  This is because we perform a binary search in the get() function.
#
# Space Complexity: O(K * N), where K is the number of unique keys and
#                   N is the average number of timestamp-value pairs per key.
#                   This is because for each key, you are storing
#                   a dictionary of timestamps and values
#                   or a list of timestamp-value tuples.


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return "" if right < 0 else values[right][1]


class MyTimeMap:
    # The following has the same time and space complexity mentioned at the beginning.
    # However, this is faster since it retrieves the result in O(1) time using hashing
    # in the best-case scenario (when the exact timestamp is present).
    # But the trade-off is we create two data structures
    # (time_map and time_map_for_search),
    # though this won't affect the space complexity (O(2*M*N) = O(M*N)).
    def __init__(self):
        self.time_map = {}
        self.time_map_for_searching = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, {})[timestamp] = value
        tuple = (timestamp, value)
        self.time_map_for_searching.setdefault(key, []).append(tuple)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        if timestamp in self.time_map[key]:
            return self.time_map[key][timestamp]
        else:
            length = len(self.time_map_for_searching[key])
            if length == 1:
                if timestamp > self.time_map_for_searching[key][0][0]:
                    return self.time_map_for_searching[key][0][1]

            left = 0
            right = length - 1
            while left <= right:
                pivot = (left + right) // 2
                if timestamp > self.time_map_for_searching[key][pivot][0]:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return self.time_map_for_searching[key][right][1] if right >= 0 else ""


# Test cases
time_map = TimeMap()
time_map.set("foo", "bar", 1)
assert time_map.get("foo", 1) == "bar"
time_map.set("foo", "bar2", 4)
assert time_map.get("foo", 3) == "bar"
assert time_map.get("foo", 4) == "bar2"
assert time_map.get("foo", 5) == "bar2"
print("All test cases passed!")
