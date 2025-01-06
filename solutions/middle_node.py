# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fp, sp = head, head
        
        while fp and fp.next:
            if fp.next.next:
                fp = fp.next.next
            else:
                fp = fp.next
            
            sp = sp.next
            
        return sp