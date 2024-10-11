// Date of Last Practice: May 16, 2024
//
// Time Complexity: O(N), where N is the total number of nodes in the linked list 1 and 2.
//                  This is because the solution iterates all the nodes in the linked list.
//
// Space Complexity: O(1).This is because it uses a constant amount of additional space.
//                   The method only utilizes a variable(current_result),
//                   regardless of the size of the input linked list.

// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var mergeTwoLists = function (list1, list2) {

    let curResult = new ListNode()
    let curHead = curResult

    while (list1 !== null && list2 != null) {
        if (list1.val <= list2.val) {
            curResult.next = list1
            list1 = list1.next
        }
        else {
            curResult.next = list2
            list2 = list2.next
        }
        curResult = curResult.next
    }

    curResult.next = list1 !== null ? list1 : list2

    return curHead.next
};

module.exports = { mergeTwoLists, ListNode }