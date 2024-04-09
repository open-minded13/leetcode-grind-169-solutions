from collections import deque
from typing import List

# Date of Last Practice: Mar 16, 2024
#
# Time Complexity: O(N+K), where N is the number of rooms, and K is the total number of keys.
#                  The sum of all keys (rooms[i].length) across all rooms is bounded by 3000,
#                  and each key leads to a room that will be visited at most once.
#
# Space Complexity: O(N+K), where N is the number of rooms, and K is the total number of keys.
#                   The visited_room set will at most contain n elements if all rooms are visited.
#                   The key_queue can at most contain all the keys found in the rooms at any point.


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Initialize a queue for BFS and a set to keep track of visited rooms
        key_queue = deque(rooms[0])
        visited_room = {0}

        while key_queue:
            # Pop the first key from the queue
            room_to_open = key_queue.popleft()
            if room_to_open in visited_room:
                continue
            # Add all new keys found in the room to the queue
            for key in rooms[room_to_open]:
                if key not in visited_room:
                    key_queue.append(key)
            # Mark the current room as visited
            visited_room.add(room_to_open)

        # If all rooms have been visited, return True
        return len(visited_room) == len(rooms)


# Test cases
sol = Solution()

# Test case 1: Possible to visit all rooms
rooms1 = [[1], [2], [3], []]
assert sol.canVisitAllRooms(rooms1) == True

# Test case 2: Impossible to visit room 2
rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
assert sol.canVisitAllRooms(rooms2) == False

# Example of a more complex test case
rooms3 = [[1, 2, 3], [4], [5], [6], [7], [8], [9], [10], [11], [], [], []]
assert sol.canVisitAllRooms(rooms3) == True

print("All tests passed!")
