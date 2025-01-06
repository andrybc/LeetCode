# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# A combination of finding the middle of the linked list with two pointers and reversing a linkelist to compare both halves
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        fp, sp = head , head
        
        if not head or  not head.next:
            return True
        
        while fp and fp.next:
            fp = fp.next.next
           
           # print(sp.val)
          
            sp = sp.next
           
        
        if(fp):
            sp = sp.next
            
        new_head = None
        current_node = sp
        
        while current_node:
            next_node = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = next_node


        while new_head:
            if(head.val != new_head.val):
                return False
            new_head = new_head.next
            head = head.next

            

        return True