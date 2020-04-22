# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        end1 = end2 = False
        val1 = val2 = 0
        if l1 != None:
            val1 = l1.val
        else:
            end1 = True

        if l2 != None:    
            val2 = l2.val
        else:
            end2 = True 

        if end1 != True or end2 != True:
            head = ListNode(0)
            tmp = head
        else:
            head = None

        while end1 != True or end2 != True:

            if end1 == False and end2 == True:
                tmp.val = val1
                l1 = l1.next
            elif end1 == True and end2 == False:
                tmp.val = val2
                l2 = l2.next
            elif end1 == False and end2 == False:
                if val1 > val2:
                    tmp.val = val2
                    l2 = l2.next
                else:
                    tmp.val = val1
                    l1 = l1.next
            else:
                pass
            
            if l1 != None:
                val1 = l1.val
            else:
                end1 = True

            if l2 != None:    
                val2 = l2.val
            else:
                end2 = True  

            if end1 == True and end2 == True:
                break
            else:
                tmp.next = ListNode(0)
                tmp = tmp.next
        
        return head

sol = Solution()
head_l1 = ListNode(1)
head_l2 = ListNode(1)

tmp = ListNode(2)
head_l1.next = tmp
tmp = ListNode(4)
head_l1.next.next = tmp
tmp = ListNode(3)
#head_l2.next = tmp
tmp = ListNode(4)
#head_l2.next.next = tmp

print(sol.mergeTwoLists(head_l2, None))

