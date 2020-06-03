# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode(0)
        
        while (l1 is not None) and (l2 is not None):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else: # if l2.val < l1.val
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            #print('cur', cur)
            #print('res', res)    
        
        if (l1 is None):
            #print(l2)
            cur.next = l2  
        elif (l2 is None):
            #print(l1)
            cur.next = l1
            
        return res.next
