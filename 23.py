class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def twoList(self, l1, l2):
        rtn = ListNode(0)
        head = rtn
        while l1 != None or l2 != None:
            if l1!= None and l2 !=None:
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

    def merge2List(self, lis):
        if not lis:
            return None
        if len(lis) < 2:
            return lis[0]
        if len(lis) == 2:
            return self.twoList(lis[0], lis[1])
        else:
            return self.twoList(self.merge2List(lis[:len(lis)/2]), self.merge2List(lis[len(lis)/2:]))

    def mergeKlists(self, lists):
        return self.merge2List(lists)

class Solution2(object):
    def twoList(self, l1, l2):
        rtn = ListNode(0)
        head = rtn
        while l1!=None or l2!= None:
            if l1 != None and l2!=None:
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

    def merge2List(self, lis):
        if not lis:
            return None
        if len(lis) < 2:
            return lis[0]

        if len(lis) == 2:
            return self.twoList(lis[0], lis[1])
        else:
            return self.twoList(self.merge2List(lis[:len(lis)/2]), self.merge2List(lis[len(lis)/2:]))

    def mergeKlist(self, lists):
        return self.merge2List(lists)