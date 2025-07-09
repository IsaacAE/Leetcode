# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = l1
        j = l2
        r = 0
        k = 0
        node = ListNode()
        p = node
    
        while i != None and j != None:
            k = i.val + j.val + r
            r = 0
            if k >= 10:
                r = k // 10
                k = k % 10

            p.next = ListNode(k)   
            i = i.next
            j = j.next
            p = p.next        

        while j!= None:
            k = 0 + j.val + r
            r=0
            if k >= 10:
                r = k // 10
                k = k % 10
            p.next = ListNode(k)   
            j = j.next
            p = p.next   


        while i!= None:
            k = i.val + 0 + r
            r=0
            if k >= 10:
                r = k // 10
                k = k % 10
            p.next = ListNode(k)   
            i = i.next
            p = p.next 

        if r != 0:
            p.next = ListNode(r)
            

        return node.next