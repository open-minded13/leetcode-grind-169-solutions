from collections import defaultdict

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


class SparseVector:
    def __init__(self, nums):
        # Step 1: Initialize sparse vector representation
        self.sparse_vector = defaultdict(int)
        self.non_zero_set = set()
        for index, num in enumerate(nums):
            if num != 0:
                self.sparse_vector[index] = num
                self.non_zero_set.add(index)

    def dotProduct(self, vec):
        # Step 2: Compute dot product of two sparse vectors
        dot_product = 0
        for index in self.non_zero_set:
            if index in vec.non_zero_set:
                dot_product += self.sparse_vector[index] * vec.sparse_vector[index]
        return dot_product


# Step 3: Test cases with assertions
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    assert v1.dotProduct(v2) == 8, "Test Case 1 Failed"

    # Test Case 2
    nums1 = [0, 1, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    assert v1.dotProduct(v2) == 0, "Test Case 2 Failed"

    # Test Case 3
    nums1 = [0, 1, 0, 0, 2, 0, 0]
    nums2 = [1, 0, 0, 0, 3, 0, 4]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    assert v1.dotProduct(v2) == 6, "Test Case 3 Failed"

    print("All test cases passed!")
