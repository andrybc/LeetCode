 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # fp, sp = head, head
        
        # if not head or head.next == None:
        #     return False
            
        # while fp.next != None:
        #     if fp.next.next != None:
        #         fp = fp.next.next
        #     else:
        #         return False
            
        #     if fp == sp:
        #         return True
            
        #     sp = sp.next
            
            
        # return False
        
        #simplified
        
        fp, sp = head, head
            
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            
            if fp == sp:
                return True
            
            
        return False