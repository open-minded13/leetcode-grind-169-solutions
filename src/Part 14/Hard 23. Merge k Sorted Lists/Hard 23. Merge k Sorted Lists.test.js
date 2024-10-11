const { mergeKLists, ListNode } = require('./Hard 23. Merge k Sorted Lists');

describe('mergeKLists', () => {
    it('should return null when the input array is empty', () => {
        expect(mergeKLists([])).toBeNull();
    });

    it('should return the only list when the input array contains one list', () => {
        let list1 = new ListNode(1);
        expect(mergeKLists([list1])).toEqual(list1);
    });

    it('should return null when all lists in the input array are null', () => {
        expect(mergeKLists([null, null, null])).toBeNull();
    });

    it('should return the merged list when the input array contains two lists', () => {
        let list1 = new ListNode(1, new ListNode(3));
        let list2 = new ListNode(2, new ListNode(4));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        expect(mergeKLists([list1, list2])).toEqual(expectedResult);
    });

    it('should return the merged list when the input array contains three lists', () => {
        let list1 = new ListNode(1, new ListNode(3));
        let list2 = new ListNode(2, new ListNode(4));
        let list3 = new ListNode(5, new ListNode(6));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        expect(mergeKLists([list1, list2, list3])).toEqual(expectedResult);
    });

    it('should return the merged list when the input array contains duplicate values', () => {
        let list1 = new ListNode(1, new ListNode(2));
        let list2 = new ListNode(2, new ListNode(2));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(2))));
        expect(mergeKLists([list1, list2])).toEqual(expectedResult);
    });

    it('should return the merged list when the input array contains lists of different lengths', () => {
        let list1 = new ListNode(1);
        let list2 = new ListNode(2, new ListNode(3));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3)));
        expect(mergeKLists([list1, list2])).toEqual(expectedResult);
    });

    it('should correctly handle large inputs', () => {
        let list1 = new ListNode(1);
        let list1_head = list1
        let list2 = new ListNode(2);
        let list2_head = list2
        for (let i = 1; i < 10000; i++) {
            list1.next = new ListNode(i * 2 + 1);
            list2.next = new ListNode(i * 2 + 2);
            list1 = list1.next;
            list2 = list2.next;
        }
        let result = mergeKLists([list1_head, list2_head]);
        let current = result;
        for (let i = 0; i < 20000; i++) {
            expect(current.val).toBe(i + 1);
            current = current.next;
        }
    });
});