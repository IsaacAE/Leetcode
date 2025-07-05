# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        

        i = list1
        j = list2
        

        if not i:
            return list2
        
        if not j:
            return list1

        head = ListNode()

        if i.val <= j.val:
            head = ListNode(i.val)
            i = i.next
        else:
            head = ListNode(j.val)
            j = j.next

        p = head


        while i is not None and j is not None:
            if i.val < j.val:
                
                p.next = ListNode(i.val)
                p = p.next
                i = i.next
                
            
            else:
                p.next = ListNode(j.val)
                p = p.next
                j = j.next

        if i is None:
            p.next = j
        else:
            p.next= i
               
       
        
        return head
                
            