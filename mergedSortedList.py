from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def compare(self, x):
        return x.val if x is not None else None

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None

        i = 0
        while i < len(lists):
            if lists[i] is None:
                lists.pop(i)
            else:
                i += 1

        if lists is not None and len(lists) > 0:
            head = ListNode(0)
            ret = head
        else:
            ret = None

        while len(lists) > 0:

            try:
                tmp_node = min(lists, key=lambda x : x.val)
            except:
                break

            i = lists.index(tmp_node)
            lists[i] = lists[i].next
            if lists[i] == None:
                lists.pop(i)

            head.val = tmp_node.val

            if len(lists) == 0 or lists is None:
                break
            else:
                head.next = ListNode(0)    
                head = head.next            

        
        return ret

sol = Solution()

input_str = [None, [0], None]

input_list = []

for il in input_str:
    head = ListNode(0)
    tmp = head

    if il is not None:
        for x in il:
            tmp.val = x
            if x != il[len(il)-1]:
                tmp.next = ListNode(0)
                tmp = tmp.next
        input_list.append(head)
    else:
        input_list.append(None)

print(sol.mergeKLists(input_list))
