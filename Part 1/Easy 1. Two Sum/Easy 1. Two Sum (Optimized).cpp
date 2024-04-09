// Time complexity: O(N);
// Space Complexity: O(N);
// Overall, the time complexity of this solution is O(n) since it only iterates over the input vector once.
// The space complexity is also O(n) since the unordered_map can store up to all elements of the input vector.

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> two_sum(vector<int> &nums, int target)
    {
        // A new unordered_map called 'mp' is created to store the key-value pairs.
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++)
        {
            // For each element, the code checks if 'target - nums[i]' exists as a key in the unordered_map.
            // If it doesn't exist, the current element 'nums[i]' is added as a key and its index 'i' is added
            // as a value to the unordered_map. This means that in future iterations,
            // if another element is found that when added to the current element equals 'target',
            // the index of the current element can be retrieved in constant time.
            if (mp.find(target - nums[i]) == mp.end())
            {
                mp[nums[i]] = i;
            }
            // If it does exist, this means that we have found the pair of indices that add up to the target value.
            // So, the current index 'i' is returned along with
            // the index of the existing key-value pair 'mp[target - nums[i]]'.
            else
            {
                return {mp[target - nums[i]], i};
            }
        }
        return {-1, -1};
    }
};

int main()
{

    vector<int> nums = {4, 5, 2, 3};
    int target = 9;

    Solution solution;
    vector<int> result = solution.two_sum(nums, target);

    if (!result.empty())
    {
        cout << result[0] << " and " << result[1] << endl;
    }
    else
    {
        cout << "Not Found!" << endl;
    }
}