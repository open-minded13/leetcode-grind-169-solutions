const { mergeTwoLists, ListNode } = require('./Easy 21. Merge Two Sorted Lists');

function listToArray(list) {
    const result = [];
    while (list !== null) {
        result.push(list.val);
        list = list.next;
    }
    return result;
}

describe('mergeTwoLists - Edge Cases', () => {
    it('should return null when both lists are null', () => {
        expect(mergeTwoLists(null, null)).toBeNull();
    });

    it('should return the second list when the first list is null and second list has one element', () => {
        let list2 = new ListNode(1);
        expect(mergeTwoLists(null, list2)).toEqual(list2);
    });

    it('should return the second list when the first list is null and second list has multiple elements', () => {
        let list2 = new ListNode(1, new ListNode(2, new ListNode(3)));
        expect(mergeTwoLists(null, list2)).toEqual(list2);
    });

    it('should return the first list when the second list is null and first list has one element', () => {
        let list1 = new ListNode(1);
        expect(mergeTwoLists(list1, null)).toEqual(list1);
    });

    it('should return the first list when the second list is null and first list has multiple elements', () => {
        let list1 = new ListNode(1, new ListNode(2, new ListNode(3)));
        expect(mergeTwoLists(list1, null)).toEqual(list1);
    });

    it('should return the merged list when both lists have one element each with the same value', () => {
        let list1 = new ListNode(1);
        let list2 = new ListNode(1);
        let expectedResult = new ListNode(1, new ListNode(1));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have one element each with different values', () => {
        let list1 = new ListNode(1);
        let list2 = new ListNode(2);
        let expectedResult = new ListNode(1, new ListNode(2));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when first list has multiple elements and second list has one element', () => {
        let list1 = new ListNode(1, new ListNode(3, new ListNode(5)));
        let list2 = new ListNode(2);
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(5))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when first list has one element and second list has multiple elements', () => {
        let list1 = new ListNode(2);
        let list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have multiple elements with interleaved values', () => {
        let list1 = new ListNode(1, new ListNode(3, new ListNode(5)));
        let list2 = new ListNode(2, new ListNode(4, new ListNode(6)));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have multiple elements and one list is entirely smaller', () => {
        let list1 = new ListNode(1, new ListNode(2, new ListNode(3)));
        let list2 = new ListNode(4, new ListNode(5, new ListNode(6)));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have multiple elements and one list is entirely larger', () => {
        let list1 = new ListNode(4, new ListNode(5, new ListNode(6)));
        let list2 = new ListNode(1, new ListNode(2, new ListNode(3)));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have multiple elements with some duplicate values', () => {
        let list1 = new ListNode(1, new ListNode(2, new ListNode(2)));
        let list2 = new ListNode(2, new ListNode(3, new ListNode(4)));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(2, new ListNode(3, new ListNode(4))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when both lists have multiple elements with all duplicate values', () => {
        let list1 = new ListNode(1, new ListNode(2, new ListNode(3)));
        let list2 = new ListNode(1, new ListNode(2, new ListNode(3)));
        let expectedResult = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(3, new ListNode(3))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when first list is significantly longer than the second list', () => {
        let list1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        let list2 = new ListNode(2);
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });

    it('should return the merged list when second list is significantly longer than the first list', () => {
        let list1 = new ListNode(1);
        let list2 = new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))));
        let expectedResult = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        expect(listToArray(mergeTwoLists(list1, list2))).toEqual(listToArray(expectedResult));
    });
});
