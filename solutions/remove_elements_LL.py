# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        emptyList = None
        if not head:
            return head
        
        if not head.next:
            if head and head.val == val: 
                return emptyList
            elif head and head.val !=val:
                return head
            
        fp , sp = head.next , head
        
        while fp and fp.next:
            if fp.val == val:
                next_node = fp.next
                sp.next = next_node
                fp = next_node
                
            fp = fp.next
            sp = sp.next
            
        
        return head