// Date of Last Practice: May 17, 2024

// Time Complexity: O(N), where N is the number of nodes in the linked list.
//                  This is because the worst case of the Floyd's Cycle Finding Algorithm
//                  iterates all the nodes in the linked list.

// Space Complexity: O(1).This is because it uses a constant amount of additional space.
//                   The method only utilizes a few variables(fast, slow),
//                   regardless of the size of the input linked list.

var hasCycle = function (head) {
    if (!head || !head.next || !head.next.next) {
        return false;
    }
    let slow = head;
    let fast = head.next.next;
    while (slow !== fast) {
        if (!fast.next || !fast.next.next) {
            return false;
        }
        fast = fast.next.next;
        slow = slow.next;
    }
    return true;
};

// var hasCycle = function (head) {
//     if (!head || !head.next || !head.next.next) {
//         return false;
//     }

//     let slow = head;
//     let fast = head.next.next;
//     let startTime = Date.now();

//     while (slow !== fast) {
//         if (!fast.next || !fast.next.next) {
//             return false;
//         }

//         // Timeout mechanism: stop execution after 10 seconds
//         if (Date.now() - startTime > 100) {
//             throw new Error('Timeout exceeded');
//         }

//         fast = fast.next.next;
//         slow = slow.next;
//     }

//     return true;
// };

// module.exports = hasCycle