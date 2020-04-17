/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = NULL;
        ListNode *tmp = NULL, *tmp2 = NULL;
        bool carry = false, end_l1 = false, end_l2 = false;
        int val = 0, val1, val2;
        
        while (l1 || l2)
        {
            val1 = (l1!=NULL) ? l1->val : 0;
            val2 = (l2!=NULL) ? l2->val : 0;
                     
            val = val1 + val2 + carry;
            
            carry = false;
            
            if (val >= 10)
            {
                carry = true;
                val -= 10;
            }
            
            tmp2 = tmp;
            tmp = new ListNode(val);
            
            if (tmp2 != NULL)
                tmp2->next = tmp; 
            else
                head = tmp;
            
            if (l1 != NULL)
                l1 = l1->next;
            if (l2 != NULL)
                l2 = l2->next;
        }
        
        if (carry)
        {
            tmp2 = tmp;
            tmp = new ListNode(carry);
            tmp2->next = tmp;
        }
        
        return head;
    }
};