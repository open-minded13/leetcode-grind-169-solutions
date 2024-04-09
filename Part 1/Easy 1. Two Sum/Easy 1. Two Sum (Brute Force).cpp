// Complexity
// Time complexity: O(N^2);
// Space Complexity: O(1);

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    Solution solution;
    vector<int> result = solution.twoSum(nums, target);
    if (!result.empty())
    {
        cout << "Indices of two numbers that add up to " << target << " are: " << result[0] << ", " << result[1] << endl;
    }
    else
    {
        cout << "No two numbers found that add up to " << target << endl;
    }
}
