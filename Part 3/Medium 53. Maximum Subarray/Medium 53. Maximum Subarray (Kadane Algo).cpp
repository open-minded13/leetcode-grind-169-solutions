// Complexity Analysis
//
// Time Complexity: O(n) where n is the size of the nums vector
//                  because it uses a single for loop to iterate over the vector.
//
// Space Complexity: O(1) because it uses a constant amount of extra space to store two integers
//                   (sum and max_sum).

#include <iostream>
#include <vector>
// It defines INT_MAX and INT_MIN.
#include <limits.h>

using namespace std;

// Optimized Solution: Kadane's Algo
class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int sum = 0;
        int max_sum = INT32_MIN;

        for (int i = 0; i < nums.size(); i++)
        {
            sum = max(nums[i], sum + nums[i]);
            max_sum = max(sum, max_sum);
        }

        return max_sum;
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