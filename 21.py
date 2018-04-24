class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        rtn = ListNode(0)
        head = rtn
        while(l1 != None) or (l2 != None):
            if l1!=None and l2!=None:
                if l1.val < l2.val:
                    rtn.next = l1
                    rtn = rtn.next
                    l1 = l1.next
                else:
                    rtn.next = l2
                    rtn = rtn.next
                    l2 = l2.next

            elif l1 != None:
                rtn.next = l1
                break

            else:
                rtn.next = l2
                break

        return head.next

class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        rtn = ListNode(0)
        head = rtn
        while(l1 != None) or (l2!=None):
            if l1!= None and l2!=None:
                if l1.val < l2.val:
                    rtn.next = l1
                    rtn = rtn.next
                    l1 = l1.next

                else:
                    rtn.next = l2
                    rtn = rtn.next
                    l2 = l2.next
                    
            elif l1 != None:
                rtn.next = l1
                break

            else:
                rtn.next = l2
                break
        return head.next