// var hasCycle = function (head) {
//     if (!head || !head.next || !head.next.next) {
//         return false;
//     }
//     let slow = head;
//     let fast = head.next.next;
//     while (slow !== fast) {
//         if (!fast.next || !fast.next.next) {
//             return false;
//         }
//         fast = fast.next.next;
//         slow = slow.next;
//     }
//     return true;
// };

var hasCycle = function (head) {
    if (!head || !head.next || !head.next.next) {
        return false;
    }

    let slow = head;
    let fast = head.next.next;
    let startTime = Date.now();

    while (slow !== fast) {
        if (!fast.next || !fast.next.next) {
            return false;
        }

        // Timeout mechanism: stop execution after 10 seconds
        if (Date.now() - startTime > 100) {
            throw new Error('Timeout exceeded');
        }

        fast = fast.next.next;
        slow = slow.next;
    }

    return true;
};

module.exports = hasCycle