// Complexity Analysis
//
// Time Complexity: O(n)
// The time complexity of this solution is O(n),
// where n is the size of the input vector.
// This is because the algorithm goes through the input vector twice,
// once from left to right and once from right to left,
// performing constant time operations at each step.
//
// Space Complexity: O(n), or O(1) if the output array does not count
// The space complexity is also O(n)
// since the algorithm uses an output vector of size n and two constant variables,
// left_product and right_product.
// The output vector is the only space used that scales with the input size.

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Some commonly used functions in std::vector:
//
// push_back(value) - adds an element to the end of the vector.
// pop_back() - removes the last element from the vector.
// size() - returns the number of elements in the vector.
// empty() - returns true if the vector is empty, false otherwise.
// clear() - removes all elements from the vector.
// resize(size) - changes the size of the vector. If the new size is greater than the current size,
//                new elements are default-constructed. If the new size is less than the current size,
//                elements at the end of the vector are removed.
// reserve(capacity) - increases the capacity of the vector to at least the specified size,
//                     but does not change the size of the vector.
// shrink_to_fit() - reduces the capacity of the vector to fit its size.
// operator[](index) - returns a reference to the element at the given index.
// at(index) - returns a reference to the element at the given index,
//             and throws a std::out_of_range exception if the index is out of range.
// front() - returns a reference to the first element in the vector.
// back() - returns a reference to the last element in the vector.
// erase(iterator) - removes the element pointed to by the iterator from the vector.
// insert(iterator, value) - inserts an element with the given value at the position pointed to by the iterator.
// begin() - returns an iterator pointing to the first element in the vector.
// end() - returns an iterator pointing to one past the last element in the vector.
//
// Note that std::vector is a dynamic array that can resize itself automatically
// as elements are added or removed. It provides constant-time access to elements by their index,
// and is a very efficient data structure for adding and removing elements from the back of the array.

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int size = nums.size();
        vector<int> output(size, 1);

        int left_product = 1;
        for (int i = 0; i < size; i++)
        {
            output[i] = output[i] * left_product;
            left_product = left_product * nums[i];
        }

        int right_product = 1;
        for (int i = size - 1; i >= 0; i--)
        {
            output[i] = output[i] * right_product;
            right_product = right_product * nums[i];
        }

        return output;
    }
};

// The time complexity of this solution is O(n), where n is the length of the input vector nums.
// This is because we iterate over the input vector three times,
// each time performing constant-time operations.
// The space complexity is also O(n),
// as we use two unordered maps to store the intermediate products
// from the beginning and end of the input vector. The output vector also has size n.
class My_First_Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        unordered_map<int, int> product_from_0_to_i;
        for (int i = 0; i < nums.size(); i++)
        {
            if (i == 0)
            {
                product_from_0_to_i.insert({i, nums[i]});
            }
            else if (i >= 1)
            {
                int product_from_0_to_i_minus_1 = product_from_0_to_i[i - 1];
                product_from_0_to_i.insert({i, nums[i] * product_from_0_to_i_minus_1});
            }
        }

        unordered_map<int, int> product_from_size_minus_1_to_i;
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            if (i == nums.size() - 1)
            {
                product_from_size_minus_1_to_i.insert({i, nums[i]});
            }
            else if (i < nums.size() - 1)
            {
                int product_from_size_minus_1_to_i_plus_1 = product_from_size_minus_1_to_i[i + 1];
                product_from_size_minus_1_to_i.insert({i, nums[i] * product_from_size_minus_1_to_i_plus_1});
            }
        }

        vector<int> output;
        for (int i = 0; i < size(nums); i++)
        {
            if (i == 0)
            {
                int product_from_size_minus_1_to_i_plus_1 = product_from_size_minus_1_to_i[i + 1];
                output.push_back(product_from_size_minus_1_to_i_plus_1);
            }
            else if (i == size(nums) - 1)
            {
                int product_from_0_to_i_minus_1 = product_from_0_to_i[i - 1];
                output.push_back(product_from_0_to_i_minus_1);
            }
            else
            {
                int product_from_0_to_i_minus_1 = product_from_0_to_i[i - 1];
                int product_from_size_minus_1_to_i_plus_1 = product_from_size_minus_1_to_i[i + 1];
                output.push_back(product_from_0_to_i_minus_1 * product_from_size_minus_1_to_i_plus_1);
            }
        }

        return output;
    }
};

int main()
{
    vector<int> nums{1, 2, 3, 4};
    Solution sol;
    vector<int> answer = sol.productExceptSelf(nums);
    for (int i = 0; i < answer.size(); i++)
    {
        cout << answer[i] << " ";
    }
    cout << endl;
    return 0;
}
