const MyQueue = require('./Easy 232. Implement Queue using Stacks');

describe('MyQueue', () => {
    // Test Case 1: Verify if the queue is empty after initialisation.
    test('queue is empty after initialization', () => {
        const queue = new MyQueue();
        expect(queue.empty()).toBe(true);
    });

    // Test Case 2: Verify that pushing an element updates the queue.
    test('push element to the queue', () => {
        const queue = new MyQueue();
        queue.push(1);
        expect(queue.empty()).toBe(false);
    });

    // Test Case 3: Check if pop() operates correctly on a single element queue.
    test('pop element from the queue', () => {
        const queue = new MyQueue();
        queue.push(2);
        expect(queue.pop()).toBe(2);
        expect(queue.empty()).toBe(true);
    });

    // Test Case 4: Ensure that the peek function correctly returns the top element without removing it.
    test('peek at the element in the queue', () => {
        const queue = new MyQueue();
        queue.push(3);
        expect(queue.peek()).toBe(3);
        expect(queue.empty()).toBe(false);
    });

    // Test Case 5: Check for null when popping from an empty queue
    test('pop from empty queue should return null', () => {
        const queue = new MyQueue();
        expect(queue.pop()).toBe(null);
    });

    // Test Case 6: Check for null when peeking from an empty queue.
    test('peek from empty queue should return null', () => {
        const queue = new MyQueue();
        expect(queue.peek()).toBe(null);
    });

    // Test Case 7: Verify if the queue is empty after multiple pops
    test('queue should be empty after multiple pops', () => {
        const queue = new MyQueue();
        queue.push(5);
        queue.push(6);
        queue.pop();
        queue.pop();
        expect(queue.empty()).toBe(true);
    });

    // Test Case 8: Check for correctness after multiple push and pops
    test('multiple push and pop', () => {
        const queue = new MyQueue();
        queue.push(5);
        queue.push(6);
        queue.push(7);
        expect(queue.pop()).toBe(5);
        expect(queue.peek()).toBe(6);
        queue.push(8);
        expect(queue.peek()).toBe(6);
        expect(queue.pop()).toBe(6);
        expect(queue.pop()).toBe(7);
        expect(queue.pop()).toBe(8);
    });

    // Test Case 9: Verify if empty() works correctly after multiple push and pops.
    test('queue should be empty after multiple push and pops', () => {
        const queue = new MyQueue();
        queue.push(5);
        queue.push(6);
        queue.push(7);
        expect(queue.pop()).toBe(5);
        queue.push(8);
        expect(queue.pop()).toBe(6);
        expect(queue.pop()).toBe(7);
        expect(queue.pop()).toBe(8);
        expect(queue.empty()).toBe(true);
    });

    //Test Case 10: Check if null is handle correctly after multiple pops.
    test('queue should handle multiple pops and return null', () => {
        const queue = new MyQueue();
        queue.pop()
        queue.pop()
        queue.pop()
        expect(queue.pop()).toBe(null);
        expect(queue.peek()).toBe(null);
    });
});