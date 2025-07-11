# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        k = head.val
        p = head
        node = ListNode(k)
        head_new = node

        while p != None:
            if p.val > k:
                k = p.val
                node.next = ListNode(k)
                node= node.next
            p = p.next

        return head_new
                
        