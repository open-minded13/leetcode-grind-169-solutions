#include <iostream>
#include <vector>
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

int main()
{
    vector<int> nums = {2, 7, 11, 15};

    nums.push_back(16);
    cout << "nums[4]: " << nums[4] << endl;
    cout << "nums.back(): " << nums.back() << endl;

    int &back = nums.back();
    int back_copy = nums.back();
    back = 33;
    cout << "back = nums.back()'s alias = nums[4]: " << back << endl;
    cout << "back_copy = nums.back()'s duplicate != nums[4]: " << back_copy << endl;

    int end_minus_1 = *(nums.end() - 1);
    cout << "*nums.end(): " << *nums.end() << endl;
    cout << "*(nums.end()-1): " << *(nums.end() - 1) << endl;
    cout << "end_minus_1 = *(nums.end()-1) = nums[4]: " << end_minus_1 << endl;

    vector<int> A = {1, 2, 3, 6};
    A.pop_back();
    cout << "A[2]: " << A[2] << endl;
    cout << "A.back(): " << A.back() << endl;
    cout << "*(A.end()-1): " << *(A.end() - 1) << endl;
    cout << "A.size(): " << A.size() << endl;
    cout << "A.empty(): " << A.empty() << endl;
    A.clear();
    cout << "A.empty() after doing A.clear(): " << A.empty() << endl;

    vector<int> B = {2, 4, 6, 8};
    B.resize(1);
    cout << "B[0]: " << B[0] << endl;
    cout << "B.back(): " << B.back() << endl;
    cout << "*(B.end()-1): " << *(B.end() - 1) << endl;
}
