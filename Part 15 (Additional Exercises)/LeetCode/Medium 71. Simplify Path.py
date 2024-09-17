# Date of Last Practice: Mar 16, 2024
#
# Time Complexity: O(N), where N is the length of the input path.
#                  The time complexity of the given solution primarily depends on
#                  the iteration over the path string once.
#
# Space Complexity: O(N), where N is the length of the input path.
#                   In the worst-case scenario (where n is the number of characters in the path),
#                   the folder_file_names list could potentially hold a fraction of the input
#                   if the path contains many valid directory names.
#                   The list size is proportional to the path's length in such scenarios.


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Step 1 - Split the path by '/'
        segments = path.split("/")

        # Step 2 - Initialize a stack to hold directory names
        stack = []

        for segment in segments:
            if segment == "..":
                # Step 3 - Pop last directory if '..' and stack is not empty
                if stack:
                    stack.pop()
            # If segment == "" (empty string), this will be considered to be False in Python.
            elif segment and segment != ".":
                # Step 3 - Push directory name into stack
                stack.append(segment)

        # Step 4 - Join the stack into a canonical path
        canonical_path = "/" + "/".join(stack)
        return canonical_path


class BadSolution:
    # While this solution is effective, it is somewhat complex and not straightforward
    # due to the detailed handling of special cases (single and double dots, slashes)

    def simplifyPath(self, path: str) -> str:
        folder_file_names = []
        dot_counter = 0

        starting_index = None
        path += "/"
        for index, char in enumerate(path):
            if dot_counter == 1 and char == "/" and index - 2 == starting_index:
                dot_counter = 0
                starting_index = None
            elif dot_counter == 2 and char == "/" and index - 3 == starting_index:
                if folder_file_names:
                    folder_file_names.pop()
                dot_counter = 0
                starting_index = None
            elif (dot_counter == 1 or dot_counter == 2) and char != ".":
                dot_counter = 0

            if char == "/":
                if starting_index is None or index - 1 == starting_index:
                    starting_index = index
                else:
                    folder_file_names.append(path[starting_index + 1 : index])
                    starting_index = index
                    dot_counter = 0
            elif char == ".":
                dot_counter += 1

        canonical_path = "/" + "/".join(folder_file_names)
        return canonical_path


# Test cases
solution = Solution()

# Test case 1
assert solution.simplifyPath("/home/") == "/home"

# Test case 2
assert solution.simplifyPath("/../") == "/"

# Test case 3
assert solution.simplifyPath("/home//foo/") == "/home/foo"

# Test case 4 - More complex path
assert solution.simplifyPath("/a/./b/../../c/") == "/c"

# Test case 5 - Path with multiple sequential slashes and dots
assert solution.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"

print("All test cases passed successfully.")
