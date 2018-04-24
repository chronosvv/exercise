class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        last_one = None

        while fast != None:
            fast.next, slow.next = slow, fast.next
            if last_one:
                last_one.next = fast
            else:
                head = fast
            last_one = slow
            slow = slow.next
            if slow:
                fast = slow.next
            else:
                break
        return head

class Solution2(object):
    def swapPairs(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        last_one = None

        while fast != None:
            fast.next, slow.next = slow, fast.next
            if last_one:
                last_one.next = fast
            else:
                head = fast
            last_one = slow
            slow = slow.next
            if slow:
                fast = slow.next
            else:
                break
        return head

