# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        new_list = ListNode(-1, head)
       
        
        current = new_list
        
        while current.next:
            if current.next.val == val:
               # print(current.next.val)
                current.next = current.next.next
            else:
                current = current.next
                
 
                   
        return new_list.next