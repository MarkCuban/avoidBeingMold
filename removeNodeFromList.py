# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def getLength(self, head):
        i = 1
        while head.next != None:
            i += 1
            head = head.next

        return i

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        tmp = head
        i = 0

        length = self.getLength(head)
        out_head = None
        relink = False

        while True:

            if i == length-n-1:
                out_head = tmp
            
            if i == length-n:
                out = tmp
                
                if out_head is None and tmp.next is not None:
                    head = tmp.next

            if i == length-n+1:
                if out_head is not None:
                    out_head.next = tmp
                    relink = True

            tmp = tmp.next

            if tmp is None:
                if relink is False and out_head is not None:
                    out_head.next = None
                break
            else:
                i += 1
        if out == head:
            out = head = None

        if out is not None:
            del(out)

        return head


sol = Solution()
MAX_LIST_NUM = 2
i = 1

head = ListNode(i)
tmp = head
while True:
    i += 1

    if i > MAX_LIST_NUM:
        break

    listnode = ListNode(i)
    tmp.next = listnode
    tmp = listnode

ret = sol.removeNthFromEnd(head, 2)

print(ret)









