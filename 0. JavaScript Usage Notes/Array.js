// Date of Practice: Apr 25, 2024

// JavaScript Array Operations Guide

// 1. Create an Array
const myArray = [1, 2, 3, 4, 5];

// 2. Access Elements in an Array
console.log(`myArray[0] = ${myArray[0]}`);  // Access the first element
console.log(`myArray[myArray.length - 1] = ${myArray[myArray.length - 1]}`);  // Access the last element

// 3. Modify Elements in an Array
myArray[0] = 6;
console.log(`myArray[0] = ${myArray[0]}`);

// 4. Add Elements to an Array
myArray.push(8);
console.log(`myArray = ${myArray}`);

// 5. Remove Elements from an Array
myArray.pop();  // Removes the last element
console.log(`myArray = ${myArray}`);

// Using splice to remove elements at a specific index
myArray.splice(2, 1);  // Removes the element at index 2
console.log(`myArray = ${myArray}`);

// 6. Iterate Over an Array
// Using forEach
myArray.forEach((item, index) => {
    console.log(`myArray's item[${index}] = ${item}`);
});

// Using for...of loop
for (const item of myArray) {
    console.log(item);
}

// Using for...in loop (not recommended for arrays)
for (const index in myArray) {
    console.log(`Using for...in, Index: ${index}, Value: ${myArray[index]}`);
}

// 7. Array Transformations
// Map function to create a new array based on existing values
const squaredArray = myArray.map(item => item ** 2);
console.log(`squaredArray = ${squaredArray}`);

// Filter function to create a new array by filtering elements based on a condition
const evenNumbers = myArray.filter(item => item % 2 === 0);
console.log(`evenNumbers = ${evenNumbers}`);

// 8. Sorting an Array
myArray.sort(); // Sorts in ascending order
console.log(`Sorted Ascending: ${myArray}`);
myArray.sort((a, b) => b - a); // Sorts in descending order
console.log(`Sorted Descending: ${myArray}`);

// 9. Checking if an Element Exists in an Array
console.log(`Does the value 3 exist in the array? ${myArray.includes(3)}`);

// 10. Searching for an Element's Index
const index = myArray.indexOf(3);
console.log(`The value 3 is at index ${index}`);

// 11. Combining Arrays
const array1 = [1, 2, 3];
const array2 = ["A", "B", "C"];
const combinedArray = array1.concat(array2);
console.log(`combinedArray = ${combinedArray}`);

// 12. Initializing a 2-D Array
const matrix2D = Array.from({ length: 3 }, (_, index) => [index + 1, index + 2, index + 3]);
console.log(`matrix2D = ${JSON.stringify(matrix2D)}`);

// Common mistake in initializing 2-D arrays
const wrongMatrix2D = Array(3).fill(Array(3).fill(-1));
console.log(`wrongMatrix2D = ${JSON.stringify(wrongMatrix2D)}`);
wrongMatrix2D[0][1] = 10;
console.log(`wrongMatrix2D = ${JSON.stringify(wrongMatrix2D)} <- Issue: all rows are updated.`);

// Correct initialization of 2-D arrays to avoid reference issues
const correctMatrix2D = Array.from({ length: 3 }, () => Array(3).fill(-1));
correctMatrix2D[0][1] = 10;
console.log(`correctMatrix2D = ${JSON.stringify(correctMatrix2D)} <- Correct: only the first row is updated.`);

// 13. Using the spread operator to copy an array
const originalArray = [1, 2, 3];
const newArray = [...originalArray];
newArray[0] = 10;
console.log(`newArray[0] = ${newArray[0]} vs originalArray[0] = ${originalArray[0]}`);

// 14. More Complex Operations Using Reduce
// For example, summing elements in an array:
const sum = myArray.reduce((acc, current) => acc + current, 0);
console.log(`Sum of myArray = ${sum}`);
