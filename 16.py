class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head

        m = n + 1
        while fast and m:
            fast = fast.next
            m -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        if m == 1:
            return head.next
        else:
            slow.next = slow.next.next
            return head

class Solution2(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head

        m = n + 1
        while fast and m:
            fast = fast.next
            m -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        if m == 1:
            return head.next
        else:
            slow.next = slow.next.next
            return head