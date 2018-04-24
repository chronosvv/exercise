class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False

        first = head.next
        if first == None:
            return False

        second = first.next
        while second != None:
            if first == second:
                return True
            first = first.next
            second = second.next
            if second == None:
                return False
            second = second.next
        return False

class Solution2(object):
    def detectCycle(self, head):
        if head == None:
            return None

        first = head.next
        if first == None:
            return None

        second = first.next
        Flag = False
        while second != None:
            if first == second:
                Flag = True
                break

            first = first.next
            second = second.next
            if second == None:
                return None
            second = second.next

        if not Flag:
            return None
        third = head
        while third != first:
            third = third.next
            first = first.next

        return third

class Solution3(object):
    def hasCycle(self, head):
        if head == None:
            return False

        first = head.next
        if first == None:
            return False

        second = first.next
        while second != None:
            if first == second:
                return True
            first = first.next
            second = second.next
            if second == None:
                return False
            second = second.next
        return False

class Solution4(object):
    def detectCycle(self, head):
        if head == None:
            return None
        first = head.next
        if first == None:
            return None
        second = first.next
        Flag = False
        while second != None:
            if first == second:
                Flag == True
                break
            first = first.next
            second = second.next
            if second == None:
                return None
            second = second.next
        if not Flag:
            return None

        third = head
        while third != first:
            third = third.next
            first = first.next

        return third
