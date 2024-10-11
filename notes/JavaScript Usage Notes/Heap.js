const { MinPriorityQueue, MaxPriorityQueue, PriorityQueue } = require('@datastructures-js/priority-queue');

// Heap Usage Note for JavaScript

// Heapify, O(N) != Heap Operation, O(log N)
// Note: Heapify is a different operation from regular heap operations.
//       Heapify has a time complexity of O(N) because during the bottom-up
//       construction of the heap, each node's movement towards its correct
//       position involves a constant number of comparisons and swaps.
//       The majority of the subtrees during construction have relatively small heights,
//       allowing us to treat the heapify operation as having a constant factor per node.
//       Thus, the linear relationship between the number of elements (N) and
//       the total number of operations for heapify results in a time complexity of O(N).
//       Additionally, the slow growth of the iterated logarithm function log* N
//       supports treating heapify as a linear operation for realistic input sizes.

// Creating a MinPriorityQueue
// const minHeap = new MinPriorityQueue(options): Creates a min priority queue.
// The time complexity for heapify is O(N) where N is the number of elements.
const minHeap = new MinPriorityQueue();

// Creating a MaxPriorityQueue
// const maxHeap = new MaxPriorityQueue(options): Creates a max priority queue.
// The time complexity for heapify is O(N) where N is the number of elements.
const maxHeap = new MaxPriorityQueue();

// Creating a PriorityQueue with complex objects
// const carsQueue = new PriorityQueue(compareFunction): Creates a priority queue with a custom comparator.
const carsQueue = new PriorityQueue((a, b) => {
    if (a.year > b.year) return -1;
    if (a.year < b.year) return 1;
    return a.price < b.price ? -1 : 1;
});

// Inserting Elements
// minHeap.enqueue(element): Inserts an element into the min priority queue.
// maxHeap.enqueue(element): Inserts an element into the max priority queue.
// carsQueue.enqueue(element): Inserts an element into the priority queue.
// Time complexity: O(log N) where N is the number of elements in the heap.
minHeap.enqueue(3);
minHeap.enqueue(1);
minHeap.enqueue(4);

maxHeap.enqueue(3);
maxHeap.enqueue(1);
maxHeap.enqueue(4);

const cars = [
    { year: 2013, price: 35000 },
    { year: 2010, price: 2000 },
    { year: 2013, price: 30000 },
    { year: 2017, price: 50000 },
    { year: 2013, price: 25000 },
    { year: 2015, price: 40000 },
    { year: 2022, price: 70000 }
];
cars.forEach(car => carsQueue.enqueue(car));

// Extracting the Minimum/Maximum Element
// minHeap.dequeue(): Extracts and returns the smallest element from the min priority queue.
// maxHeap.dequeue(): Extracts and returns the largest element from the max priority queue.
// carsQueue.dequeue(): Extracts and returns the highest priority element from the priority queue.
// Time complexity: O(log N)
const smallest = minHeap.dequeue();
console.log('Smallest element:', smallest); // 1

const largest = maxHeap.dequeue();
console.log('Largest element:', largest); // 4

console.log(carsQueue.dequeue()); // { year: 2022, price: 70000 }
console.log(carsQueue.dequeue()); // { year: 2017, price: 50000 }
console.log(carsQueue.dequeue()); // { year: 2015, price: 40000 }

// Peeking at the Minimum/Maximum Element
// minHeap.front(): Returns the smallest element without removing it from the heap.
// maxHeap.front(): Returns the largest element without removing it from the heap.
// carsQueue.front(): Returns the highest priority element without removing it from the heap.
// Time complexity: O(1)
const minElement = minHeap.front();
console.log('Current smallest element:', minElement); // 3

const maxElement = maxHeap.front();
console.log('Current largest element:', maxElement); // 3

console.log(carsQueue.front()); // { year: 2013, price: 30000 }

// Peeking at the Element with the Lowest Priority
// carsQueue.back(): Returns the lowest priority element without removing it from the heap.
// Time complexity: O(1)
console.log(carsQueue.back()); // { year: 2010, price: 2000 }

// Checking if the MinPriorityQueue/MaxPriorityQueue/PriorityQueue is Empty
// minHeap.isEmpty(): Returns true if the min priority queue is empty, false otherwise.
// maxHeap.isEmpty(): Returns true if the max priority queue is empty, false otherwise.
// carsQueue.isEmpty(): Returns true if the priority queue is empty, false otherwise.
// Time complexity: O(1)
const isMinHeapEmpty = minHeap.isEmpty();
console.log('Is the min heap empty?', isMinHeapEmpty); // false

const isMaxHeapEmpty = maxHeap.isEmpty();
console.log('Is the max heap empty?', isMaxHeapEmpty); // false

console.log(carsQueue.isEmpty()); // false

// Getting the Size of the MinPriorityQueue/MaxPriorityQueue/PriorityQueue
// minHeap.size(): Returns the number of elements in the min priority queue.
// maxHeap.size(): Returns the number of elements in the max priority queue.
// carsQueue.size(): Returns the number of elements in the priority queue.
// Time complexity: O(1)
const minHeapSize = minHeap.size();
console.log('Size of the min heap:', minHeapSize); // 2

const maxHeapSize = maxHeap.size();
console.log('Size of the max heap:', maxHeapSize); // 2

console.log(carsQueue.size()); // 3

// Clearing the MinPriorityQueue/MaxPriorityQueue/PriorityQueue
// minHeap.clear(): Removes all elements from the min priority queue.
// maxHeap.clear(): Removes all elements from the max priority queue.
// carsQueue.clear(): Removes all elements from the priority queue.
// Time complexity: O(1)
minHeap.clear();
console.log('Is the min heap empty after clearing?', minHeap.isEmpty()); // true

maxHeap.clear();
console.log('Is the max heap empty after clearing?', maxHeap.isEmpty()); // true

carsQueue.clear();
console.log(carsQueue.size()); // 0

// Creating MinPriorityQueue from Array
// MinPriorityQueue.fromArray(array, compareFunction): Creates a min priority queue from an array.
// The time complexity for heapify is O(N).
const numbers = [3, -2, 5, 0, -1, -5, 4];
const numbersQueue = MinPriorityQueue.fromArray(numbers, (a, b) => a - b);
console.log(numbersQueue.toArray()); // [-5, -2, -1, 0, 3, 4, 5]
numbersQueue.clear();

// Creating MaxPriorityQueue from Array
// MaxPriorityQueue.fromArray(array, compareFunction): Creates a max priority queue from an array.
// The time complexity for heapify is O(N).
const mpq = MaxPriorityQueue.fromArray(numbers, (a, b) => b - a);
console.log(mpq.toArray()); // [5, 4, 3, 0, -1, -2, -5]
mpq.clear();

// Handling Bids with MaxPriorityQueue
// MaxPriorityQueue(callback): Creates a max priority queue with a callback for object values.
const bidsQueue = new MaxPriorityQueue(bid => bid.value);
const bids = [
    { id: 1, value: 1000 },
    { id: 2, value: 20000 },
    { id: 3, value: 1000 },
    { id: 4, value: 1500 },
    { id: 5, value: 12000 },
    { id: 6, value: 4000 },
    { id: 7, value: 8000 }
];
bids.forEach(bid => bidsQueue.enqueue(bid));

console.log(bidsQueue.front()); // { id: 2, value: 20000 }
console.log(bidsQueue.back());  // { id: 1, value: 1000 }

console.log(bidsQueue.dequeue()); // { id: 2, value: 20000 }
console.log(bidsQueue.dequeue()); // { id: 5, value: 12000 }
console.log(bidsQueue.dequeue()); // { id: 7, value: 8000 }

bidsQueue.remove(bid => bid.id === 3); // [{ id: 3, value: 1000 }]

console.log(bidsQueue.isEmpty()); // false
console.log(bidsQueue.size());    // 3
console.log(bidsQueue.toArray()); // [{ id: 6, value: 4000 }, { id: 4, value: 1500 }, { id: 1, value: 1000 }]

for (const bid of bidsQueue) {
    console.log(bid);
}
// Iterating empties the queue
console.log(bidsQueue.size()); // 0

bidsQueue.clear();
console.log(bidsQueue.size()); // 0
console.log(bidsQueue.front()); // null
console.log(bidsQueue.dequeue()); // null
console.log(bidsQueue.isEmpty()); // true
