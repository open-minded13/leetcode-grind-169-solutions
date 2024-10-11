"""
Flatten a nested dictionary by concatenating keys.

This module defines a class Solution with a method flatten_dictionary,
which takes a nested dictionary and returns a flattened version where
the keys are concatenated with dots.

Typical usage example:

  solution = Solution()
  flattened = solution.flatten_dictionary(nested_dict)
"""

from typing import Dict, Union

# Date of Last Practice: Oct 10, 2024
#
# Time Complexity: O(N), where N is the total number of key-value pairs in the
#                  dictionary. We visit each key-value pair once.
#
# Space Complexity: O(D + N), where D is the maximum depth of the nested dictionary
#                   and N is the total number of key-value pairs in the dictionary.
#                   The space complexity is O(D + N) because we use recursion to
#                   traverse the nested dictionary. The maximum depth of the recursion
#                   is the depth of the nested dictionary. In the worst case, the
#                   dictionary is a single nested dictionary, and the depth is equal
#                   to the number of key-value pairs.


class Solution:
    """Provides a method to flatten a nested dictionary."""

    def flatten_dictionary(
        self, dictionary: Dict[str, Union[str, Dict]]
    ) -> Dict[str, str]:
        """
        Flatten a nested dictionary by concatenating nested keys with dots.

        Args:
            dictionary: A nested dictionary with string keys and values being
                        either a string or another dictionary.

        Returns:
            A flattened dictionary with concatenated keys.
        """
        flattened_dict = {}

        def dict_builder(sub_dict, cur_key):
            """Recursively build flattened dictionary from nested dictionary."""
            if isinstance(sub_dict, dict):
                for key in sub_dict:
                    new_key = cur_key
                    if key:
                        new_key = cur_key + "." + key if cur_key else key
                    dict_builder(sub_dict[key], new_key)
            else:
                flattened_dict[cur_key] = sub_dict

        dict_builder(dictionary, "")
        return flattened_dict


def main():
    """Demonstrate the Solution class and run test cases."""
    solution = Solution()

    # Test case 1
    dict_input1 = {
        "Key1": "1",
        "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"": "1"}}},
    }
    expected_output1 = {
        "Key1": "1",
        "Key2.a": "2",
        "Key2.b": "3",
        "Key2.c.d": "3",
        "Key2.c.e": "1",
    }
    assert solution.flatten_dictionary(dict_input1) == expected_output1

    # Test case 2
    dict_input2 = {"Key": {"a": "2", "b": "3"}}
    expected_output2 = {"Key.a": "2", "Key.b": "3"}
    assert solution.flatten_dictionary(dict_input2) == expected_output2

    # Test case 3
    dict_input3 = {
        "Key1": "1",
        "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"f": "4"}}},
    }
    expected_output3 = {
        "Key1": "1",
        "Key2.a": "2",
        "Key2.b": "3",
        "Key2.c.d": "3",
        "Key2.c.e.f": "4",
    }
    assert solution.flatten_dictionary(dict_input3) == expected_output3

    # Test case 4
    dict_input4 = {"": {"a": "1"}, "b": "3"}
    expected_output4 = {"a": "1", "b": "3"}
    assert solution.flatten_dictionary(dict_input4) == expected_output4

    # Test case 5
    dict_input5 = {"a": {"b": {"c": {"d": {"e": {"f": {"": "awesome"}}}}}}}
    expected_output5 = {"a.b.c.d.e.f": "awesome"}
    assert solution.flatten_dictionary(dict_input5) == expected_output5

    # Test case 6
    dict_input6 = {"a": "1"}
    expected_output6 = {"a": "1"}
    assert solution.flatten_dictionary(dict_input6) == expected_output6

    print("All test cases passed!")


if __name__ == "__main__":
    main()
