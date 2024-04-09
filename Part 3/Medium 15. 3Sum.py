# Date of Last Practice: Jun 13, 2023 -> Feb 3, 2024
#
# Time Complexity: O(N^2). Specifically, the outer loop of the nested loop iterates M times of list_of_dict_1,
#                  and the inner loop iterates a decreasing number of times
#                  for each iteration of the outer loop (but NOT M!).
#                  Though it is optimized, it is still O(M^2). In the worst case, M = N = the size of nums.
#                  As a result, the time complexity is O(N^2).
#
# Space Complexity: O(N). We used two constant extra dictionaries, positive_dict and negative_dict,
#                   to store the data of nums. They require space proportional to the size of
#                   the input array nums, which is N.


from collections import defaultdict


class Solution:
    def threeSum(self, nums):
        positive_dict = defaultdict(int)
        negative_dict = defaultdict(int)
        zeros = 0

        # Read the data
        for num in nums:
            if num > 0:
                positive_dict[num] += 1
            elif num < 0:
                negative_dict[num] += 1
            else:
                zeros += 1

        # Analyze the data
        result = []

        # For [0, 0, 0]
        if zeros >= 3:
            result.append([0, 0, 0])

        # For [0, positive, negative]
        if zeros >= 1:
            for num in positive_dict:
                if -num in negative_dict:
                    result.append([-num, 0, num])

        # For [positive_1, positive_2, negative] and [negative_1, negative_2, positive]
        for dict_1, dict_2 in (
            (positive_dict, negative_dict),
            (negative_dict, positive_dict),
        ):
            list_of_dict_1 = list(dict_1.items())
            for index, (num_1, count_of_num_1) in enumerate(list_of_dict_1):
                for num_2, count_of_num_2 in list_of_dict_1[index:]:
                    if num_1 == num_2 and count_of_num_1 > 1:
                        if -2 * num_1 in dict_2:
                            result.append([num_1, num_1, -2 * num_1])
                    if num_1 != num_2:
                        if -(num_1 + num_2) in dict_2:
                            result.append([num_1, num_2, -(num_1 + num_2)])

        return result


# Testing the solution
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)
