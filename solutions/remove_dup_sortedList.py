# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # new_list = ListNode(-200, head)
        
        # current_node = new_list
        
        # while current_node and current_node.next:
        #     #next_node = current_node.next
        #   #  print(f"comparing current node: {current_node.val} and next node: {current_node.next.val}")
        #     while current_node.next and current_node.val == current_node.next.val:
        #       #  print(f"comparing current node: {current_node.val} and next node: {current_node.next.val} inside of the loop")
        #         current_node.next = current_node.next.next
                
            
        #     current_node = current_node.next   
        #    # print(current_node.val)
            
        # return new_list.next
        current_node = head
        
        while current_node and current_node.next:
            
            while current_node.next and current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                
            
            current_node = current_node.next   
            
        return head