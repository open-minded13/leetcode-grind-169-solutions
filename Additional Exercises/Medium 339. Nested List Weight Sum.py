# Date of Last Practice: Mar 10, 2024
#
# Time Complexity: O(N), where N includes every integer and list encountered in the structure.
#                  Each element is processed once and the process involves
#                  going down the levels of nesting.
#
# Space Complexity: O(D), where D is the depth of the nested list.
#                   The maximum depth of recursion corresponds to
#                   the maximum depth of the nested list structure.
#                   In the worst case, this could be up to 50 (as per the given constraints).


class Solution:
    def depthSum(self, nestedList) -> int:
        def _calculate_sum(nested_list, level):
            sum_of_level = 0
            index = 0
            while index < len(nested_list):
                item = nested_list[index]
                if item.isInteger():
                    sum_of_level += item.getInteger() * level
                else:
                    sum_of_level += _calculate_sum(item.getList(), level + 1)
                index += 1
            return sum_of_level

        return _calculate_sum(nestedList.getList(), 1)


class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self.data = []
        elif isinstance(value, int):
            self.data = value
        else:
            raise ValueError("Unsupported type for NestedInteger")

    def isInteger(self):
        return isinstance(self.data, int)

    def add(self, elem):
        if not self.isInteger():
            if isinstance(elem, NestedInteger):
                self.data.append(elem)
            else:
                raise ValueError("Only NestedInteger objects can be added")
        else:
            raise ValueError("Cannot add to NestedInteger holding an integer")

    def setInteger(self, value):
        if isinstance(value, int):
            self.data = value
        else:
            raise ValueError("Only integer values are supported")

    def getInteger(self):
        if self.isInteger():
            return self.data
        return None

    def getList(self):
        if not self.isInteger():
            return self.data
        return None


# Test cases
sol = Solution()


# Assuming there's a way to create a NestedInteger object from a list for testing
def create_nested_list(lst):
    if isinstance(lst, int):
        return NestedInteger(lst)
    elif isinstance(lst, list):
        nested_int = NestedInteger()
        for item in lst:
            nested_int.add(create_nested_list(item))
        return nested_int
    else:
        raise ValueError("Input must be an integer or a list")


# Example 1
nestedList = create_nested_list([[1, 1], 2, [1, 1]])
assert sol.depthSum(nestedList) == 10, "Test case 1 failed."

# Example 2
nestedList = create_nested_list([1, [4, [6]]])
assert sol.depthSum(nestedList) == 27, "Test case 2 failed."

# Example 3
nestedList = create_nested_list([0])
assert sol.depthSum(nestedList) == 0, "Test case 3 failed."

print("All test cases passed!")
