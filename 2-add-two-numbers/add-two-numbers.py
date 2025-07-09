# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = l1
        j = l2
        node = ListNode((i.val+j.val) % 10 )
        head = node
        r = (i.val + j.val) // 10
    
        while i.next != None and j.next != None:
            i = i.next
            j = j.next
            value = i.val + j.val +r
            k = value % 10
            r = value // 10
            node.next = ListNode(k)   
            node = node.next        

        while j.next!= None:
            j = j.next
            value = j.val +r
            k = value % 10
            r = value // 10
            node.next = ListNode(k)   
            node = node.next 

        while i.next!= None:
            i = i.next
            value = i.val +r
            k = value % 10
            r = value // 10
            node.next = ListNode(k)   
            node = node.next 

        if r != 0:
            node.next = ListNode(r)
            

        return head