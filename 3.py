class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        increment = 0
        rtn = cal = ListNode(0)

        while l1 or l2 or increment:
            a = l1.val if l1 and l1.val else 0
            b = l2.val if l2 and l2.val else 0
            cal.val = (a + b + increment) % 10
            increment = (a + b + increment) / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or increment:
                cal.next = ListNode(0)
                cal = cal.next

        return rtn

class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        increment = 0
        rtn = cal = ListNode(0)

        while l1 or l2 or increment:
            a = l1.val if l1 and l1.val else 0
            b = l2.val if l2 and l2.val else 0
            cal.val = (a + b + increment) % 10
            increment = (a + b + increment) / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or increment:
                cal.next = ListNode(0)
                cal = cal.next

        return rtn
