const hasCycle = require("./Easy 141. Linked List Cycle")

describe('hasCycle', () => {
    class ListNode {
        constructor(val = 0, next = null) {
            this.val = val;
            this.next = next;
        }
    }

    it('should return false for an empty list', () => {
        expect(hasCycle(null)).toBe(false);
    });

    it('should return false for a single node list', () => {
        const head = new ListNode(1);
        expect(hasCycle(head)).toBe(false);
    });

    it('should return false for a two-node list', () => {
        const head = new ListNode(1, new ListNode(2));
        expect(hasCycle(head)).toBe(false);
    });

    it('should return false for a three-node list without a cycle', () => {
        const head = new ListNode(1, new ListNode(2, new ListNode(3)));
        expect(hasCycle(head)).toBe(false);
    });

    it('should return true for a three-node list with a cycle', () => {
        const node3 = new ListNode(3);
        const node2 = new ListNode(2, node3);
        const head = new ListNode(1, node2);
        node3.next = head; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    it('should return true for a four-node list with a cycle', () => {
        const node4 = new ListNode(4);
        const node3 = new ListNode(3, node4);
        const node2 = new ListNode(2, node3);
        const head = new ListNode(1, node2);
        node4.next = node2; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    it('should return true for a five-node list with a cycle', () => {
        const node5 = new ListNode(5);
        const node4 = new ListNode(4, node5);
        const node3 = new ListNode(3, node4);
        const node2 = new ListNode(2, node3);
        const head = new ListNode(1, node2);
        node5.next = head; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    it('should return false for a five-node list without a cycle', () => {
        const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        expect(hasCycle(head)).toBe(false);
    });

    it('should return true for a six-node list with a cycle', () => {
        const node6 = new ListNode(6);
        const node5 = new ListNode(5, node6);
        const node4 = new ListNode(4, node5);
        const node3 = new ListNode(3, node4);
        const node2 = new ListNode(2, node3);
        const head = new ListNode(1, node2);
        node6.next = node3; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    it('should return false for a six-node list without a cycle', () => {
        const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        expect(hasCycle(head)).toBe(false);
    });

    // Define a simple Node class for testing purposes
    class Node {
        constructor(val) {
            this.val = val;
            this.next = null;
        }
    }

    // Test case 1: Empty list
    it('should return false for an empty list', () => {
        expect(hasCycle(null)).toBe(false);
    });

    // Test case 2: Single node list
    it('should return false for a single node list', () => {
        const head = new Node(1);
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 3: Two-node list without cycle
    it('should return false for a two-node list without cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 4: Two-node list with cycle
    it('should return true for a two-node list with cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = head; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    // Test case 5: Three-node list without cycle
    it('should return false for a three-node list without cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 6: Three-node list with cycle
    it('should return true for a three-node list with cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = head.next; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    // Test case 7: Four-node list without cycle
    it('should return false for a four-node list without cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 8: Four-node list with cycle
    it('should return true for a four-node list with cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = head.next; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    // Test case 9: Five-node list without cycle
    it('should return false for a five-node list without cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 10: Five-node list with cycle
    it('should return true for a five-node list with cycle', () => {
        const head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = head.next.next; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    // Test case 11: Large list without cycle
    it('should return false for a large list without cycle', () => {
        const head = new Node(1);
        let current = head;
        for (let i = 2; i <= 1000; i++) {
            current.next = new Node(i);
            current = current.next;
        }
        expect(hasCycle(head)).toBe(false);
    });

    // Test case 12: Large list with cycle
    it('should return true for a large list with cycle', () => {
        const head = new Node(1);
        let current = head;
        for (let i = 2; i <= 1000; i++) {
            current.next = new Node(i);
            current = current.next;
        }
        current.next = head.next.next; // Create a cycle
        expect(hasCycle(head)).toBe(true);
    });

    // Test case with large list and timeout
    // it('should handle large lists and timeouts', () => {
    //     const head = new Node(1);
    //     let current = head;
    //     for (let i = 2; i <= 1000000; i++) {
    //         current.next = new Node(i);
    //         current = current.next;
    //     }
    //     current.next = head.next.next; // Create a cycle

    //     expect(() => hasCycle(head)).toThrowError('Timeout exceeded');
    // });
});