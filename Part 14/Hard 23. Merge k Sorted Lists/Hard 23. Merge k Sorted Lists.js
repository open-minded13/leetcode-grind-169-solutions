const { MinPriorityQueue } = require('@datastructures-js/priority-queue');

// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

const mergeKLists = function (lists) {
    const queue = new MinPriorityQueue((x) => x.val);

    for (const head of lists) {
        if (head) {
            queue.enqueue(head);
        }
    }

    let result = new ListNode();
    const head = result;

    while (!queue.isEmpty()) {
        const node = queue.dequeue();

        if (!node) {
            continue; // Skip if the node is undefined or null
        }

        result.next = node;
        result = result.next;

        if (node.next) {
            queue.enqueue(node.next);
        }
    }

    return head.next;
};

module.exports = { mergeKLists, ListNode };
