// Complexity Analysis
//
// Time Complexity: O(N), where N is the length of the input vector nums.
// This is because the solve function is called exactly N times,
// and each call takes constant time to execute (i.e., O(1)).
//
// Space Complexity:
// The space complexity of this solution is also O(N),
// because we are using a 2D vector dp of size 2xN to store the computed results.
// Since we only need to store the results for the current and the next state,
// we can reduce the space complexity to O(1) by using two variables
// instead of a 2D vector. However, since the maximum value of N is 3x10^4,
// which is not very large,
// the current implementation is still efficient enough in terms of space usage.

#include <iostream>
#include <vector>

// It defines INT_MAX and INT_MIN.
#include <limits.h>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        vector<vector<int>> dp(2, vector<int>(size(nums), -1));
        return solve(nums, 0, false, dp);
    }
    int solve(vector<int> &nums, int index, bool must_pick, vector<vector<int>> &dp)
    {

        if (index >= size(nums))
        {
            if (must_pick)
            {
                return 0;
            }
            else
            {
                return INT32_MIN;
            }
        }

        if (dp[must_pick][index] != -1)
        {
            return dp[must_pick][index];
        }

        if (must_pick)
        {
            return dp[must_pick][index] = max(0, nums[index] + solve(nums, index + 1, true, dp));
        }
        else
        {
            return dp[must_pick][index] = max(solve(nums, index + 1, false, dp), nums[index] + solve(nums, index + 1, true, dp));
        }
    }
};

// This code is a solution for the maximum subarray problem using dynamic programming.
// The maximum subarray problem is the task of finding the contiguous subarray
// within a one-dimensional array of numbers that has the largest sum.
class Solution_Dynamic_Programming_Memoization
{
public:
    // The solution consists of a class named "Solution" that
    // has a public method named "maxSubArray" that takes a vector of integers
    // as input and returns an integer,
    // which is the maximum sum of a subarray within the input vector.
    int maxSubArray(vector<int> &nums)
    {

        // The "maxSubArray" method initializes a 2D vector
        // named "dp" with two rows and the same number of columns as
        // the input vector, where the value of each element is initially set to -1.
        // It then calls the "solve" method with the input vector, the starting index 0,
        // a flag indicating whether the current element must be picked
        // (set to false initially), and the "dp" vector.
        vector<vector<int>> dp(2, vector<int>(size(nums), -1));
        return solve(nums, 0, false, dp);
    }

    // The "solve" method is a recursive function that takes four arguments:
    // the input vector "A", the current index "i",
    // a boolean variable "mustPick" that indicates whether the current element
    // must be picked, and the "dp" vector.
    // It returns an integer, which is the maximum sum of a subarray that starts
    // from the current index.
    int solve(vector<int> &nums, int index, bool mustPick, vector<vector<int>> &dp)
    {

        // The "solve" method first checks if the current index "i" is
        // greater than or equal to the size of the input vector "A".
        // If it is, it returns 0 if "mustPick" is true
        // (meaning that the last element was picked) and
        // -1e5 (a large negative number) otherwise.
        // This is because if "mustPick" is true,
        // we have to pick the last element even if it is negative,
        // otherwise we can skip it.
        if (index >= size(nums))
            return mustPick ? 0 : -1e5;

        // The method then checks if the value of "dp[mustPick][i]"
        // is not equal to -1. If it is not, it means that
        // the maximum sum of a subarray that starts from
        // the current index has already been calculated and
        // stored in the "dp" vector, so the method simply returns that value.
        if (dp[mustPick][index] != -1)
            return dp[mustPick][index];

        // If "mustPick" is true, the method returns the maximum of 0 and
        // the sum of the current element and the maximum sum of a subarray that
        // starts from the next index, with "mustPick" set to true.
        if (mustPick)
            return dp[mustPick][index] = max(0, nums[index] + solve(nums, index + 1, true, dp));

        // If "mustPick" is false, the method returns the maximum of
        // the maximum sum of a subarray that starts from the next index
        // with "mustPick" set to false, and the sum of the current element and
        // the maximum sum of a subarray that starts from the next index
        // with "mustPick" set to true.
        return dp[mustPick][index] = max(solve(nums, index + 1, false, dp), nums[index] + solve(nums, index + 1, true, dp));
    }
};

int main()
{
    Solution s;

    // Test case 1: [-2,1,-3,4,-1,2,1,-5,4]
    vector<int> nums1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int result1 = s.maxSubArray(nums1);
    cout << "Maximum subarray sum of [-2,1,-3,4,-1,2,1,-5,4] is: " << result1 << endl;

    // Test case 2: [1]
    vector<int> nums2 = {1};
    int result2 = s.maxSubArray(nums2);
    cout << "Maximum subarray sum of [1] is: " << result2 << endl;

    // Test case 3: [5,4,-1,7,8]
    vector<int> nums3 = {5, 4, -1, 7, 8};
    int result3 = s.maxSubArray(nums3);
    cout << "Maximum subarray sum of [5,4,-1,7,8] is: " << result3 << endl;

    return 0;
}