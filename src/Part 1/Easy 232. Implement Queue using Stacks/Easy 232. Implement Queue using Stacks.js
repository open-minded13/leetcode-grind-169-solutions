// Date of Last Practice: Mar 23, 2024

// Time Complexity: O(1), because this method gives us an amortized constant - time 
//                  peek and pop operations after an initial O(n) preprocessing time 
//                  when moving elements from the `inStack` to the`outStack`. 

//                  - Push: O(1), since there is only one push() operation, 
//                    adding an element to the back of an array (`inStack`).
//                  - Pop: O(1) amortized time complexity. 
//                  - Peek: O(1) amortized time complexity. 
//                  - Empty: O(1) worst-case time complexity.            

// Space Complexity: O(n), where n is the maximum number of elements in the queue. 

var MyQueue = function () {
    this.inStack = []
    this.outStack = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
    this.inStack.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function () {
    if (this.outStack.length === 0) {
        while (this.inStack.length) {
            this.outStack.push(this.inStack.pop())
        }
    }
    return this.outStack.length ? this.outStack.pop() : null
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function () {
    if (this.outStack.length === 0) {
        while (this.inStack.length) {
            this.outStack.push(this.inStack.pop())
        }
    }
    return this.outStack.length ? this.outStack[this.outStack.length - 1] : null
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
    if (this.outStack.length === 0 && this.inStack.length === 0) {
        return true
    }
    return false
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

module.exports = MyQueue