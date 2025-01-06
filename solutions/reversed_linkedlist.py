# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = next_node
            #head = temp
            
        return new_head