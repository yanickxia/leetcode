/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
class Solution {
    public ListNode sortList(ListNode head) {

        if (head == null) {
            return null;
        }

        ListNode mid = head;
        head = head.next;
        mid.next = null;

        if (head == null) {
            return mid;
        }

        ListNode leftHead = null;
        ListNode leftTail = null;
        ListNode rightHead = null;
        ListNode rightTail = null;

        while (head != null) {
            if (head.val < mid.val) {
                if (leftHead == null) {
                    leftHead = head;
                    leftTail = leftHead;
                } else {
                    leftTail.next = head;
                    leftTail = leftTail.next;
                }
            } else {
                if (rightHead == null) {
                    rightHead = head;
                    rightTail = rightHead;
                } else {
                    rightTail.next = head;
                    rightTail = rightTail.next;
                }
            }
            head = head.next;
        }

        if (leftTail != null) {
            leftTail.next = null;
        }
        if (rightTail != null) {
            rightTail.next = null;
        }

        ListNode lessMid = leftHead;
        ListNode biggerMid = rightHead;

        if (lessMid != null && biggerMid != null) {
            ListNode left = sortList(lessMid);
            ListNode right = sortList(biggerMid);

            findLast(left).next = mid;
            mid.next = right;

            return left;
        } else if (lessMid != null) {
            ListNode left = sortList(lessMid);
            findLast(left).next = mid;

            return left;
        } else {
            ListNode right = sortList(biggerMid);
            mid.next = right;

            return mid;
        }
    }

    private ListNode findLast(ListNode listNode) {
        while (listNode.next != null) {
            listNode = listNode.next;
        }

        return listNode;
    }
}