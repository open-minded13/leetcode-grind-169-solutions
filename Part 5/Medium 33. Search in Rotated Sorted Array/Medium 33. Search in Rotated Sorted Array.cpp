// Complexity Analysis
//
// Time Complexity: O(N), where N is the size of the input array.
//                  In the worst-case scenario, when the array is nearly sorted or completely sorted,
//                  the algorithm will have a time complexity of O(log N).
//
// Space Complexity: O(1)
//                   It uses a constant amount of additional space regardless of the size of the input array.
//                   Only a few variables are used to keep track of the indices (left, right, and pivot)
//                   and the target element, and their memory consumption remains constant.

#include <iostream>
#include <vector>

using namespace std;

// Optimized Solution: Binary Search Algorithm
class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int pivot = left + (right - left) / 2;

            if (target == nums[pivot])
            {
                return pivot;
            }

            // Note: It should be nums[left] <= nums[pivot] rather than <
            //       You should consider this situation: nums = {3, 1}, target = 1
            if (nums[left] <= nums[pivot])
            {
                if (nums[left] <= target && target < nums[pivot])
                {
                    right = pivot - 1;
                }
                else
                {
                    left = pivot + 1;
                }
            }
            else
            {
                if (nums[right] >= target && target > nums[pivot])
                {
                    left = pivot + 1;
                }
                else
                {
                    right = pivot - 1;
                }
            }
        }

        return -1;
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    int index = solution.search(nums, target);
    if (index != -1)
    {
        cout << "Target " << target << " found at index " << index << endl;
    }
    else
    {
        cout << "Target " << target << " not found in the array." << endl;
    }
    return 0;
}
