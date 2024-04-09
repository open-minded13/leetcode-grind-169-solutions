import os
from typing import List


# Date of Last Practice: Dec 17, 2023 -> Feb 7, 2024
#
# Time Complexity: O(V+E), where V is the number of courses (vertices) and
#                  E is the number of prerequisites (edges).
#                  Both solutions have a similar time complexity.
#                  They need to traverse each course and its prerequisites,
#                  leading to a time complexity of O(V+E),
#
# Space Complexity: O(V), where V is the number of rows and N is the number of columns.
#                   They both use additional data structures,
#                   including an adjacency list using a dictionary,
#                   a current_checking_path set to check the current path,
#                   and a fully_checked_vertices to track visited courses,
#                   which contributes to O(V) space complexity.
#                   The recursive stack in Solution_1 can also add
#                   up to O(V) in space complexity in the worst case.
#                   A worst-case scenario will happen when prerequisites are arranged
#                   in a linear chain: [ [1, 0], [2, 1], [3, 2], ..., [n-1, n-2] ].


class Solution_1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        current_checking_path = set()
        fully_checked_vertices = set()

        def dfs(course):
            if course in fully_checked_vertices:
                return True
            if course in current_checking_path:
                return False

            current_checking_path.add(course)
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            current_checking_path.remove(course)
            fully_checked_vertices.add(course)

            # Remember to return True, otherwise the default will return 0 or False.
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


class Solution_2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for [course, prerequisite] in prerequisites:
            graph[course].append(prerequisite)

        fully_checked_set = set()
        current_checking_path = set()

        dfs_stack = [(i, False) for i in range(numCourses)]
        while dfs_stack:
            course, is_viewed = dfs_stack.pop()
            if not is_viewed:
                if course in fully_checked_set:
                    continue
                if course in current_checking_path:
                    return False
                dfs_stack.append((course, True))
                current_checking_path.add(course)
                for prerequisite in graph[course]:
                    dfs_stack.append((prerequisite, False))
            else:
                current_checking_path.remove(course)
                fully_checked_set.add(course)
        return True


def test_solution(sol):
    assert sol.canFinish(2, [[1, 0]]) == True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) == False
    assert sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]) == True
    assert sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) == False
    assert sol.canFinish(3, [[0, 1], [0, 2], [1, 2]]) == True
    print("All test cases passed!")


# Testing Solution 1
test_solution(Solution_1())

# Testing Solution 2
test_solution(Solution_2())
