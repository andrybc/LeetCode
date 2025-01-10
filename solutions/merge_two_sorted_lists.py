# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    #     head = ListNode(0, None)

        
    #     mergelist = head
        
    #     ptr1 = list1
    #     ptr2 = list2
    #    # print(f"The current value in list1: {ptr1.val} vs the current value in list2 {ptr2.val}")
        
    #     while ptr1 or ptr2:
    #         if not ptr1:
    #                 head.next = ptr2
    #                 return mergelist.next

    #         elif not ptr2:
    #                 head.next = ptr1
    #                 return mergelist.next

                    
    #         elif ptr1.val <= ptr2.val:
    #                # print(f"The current value in list1: {ptr1.val} vs the current value in list2 {ptr2.val}")
    #                 head.next = ptr1
    #                 ptr1 = ptr1.next
    #                 head = head.next 
    #                 #print(f"the current value of head is now {head.val}")
    #         elif ptr2.val < ptr1.val:
    #                 #print(f"The current value in list1: {ptr1.val} vs the current value in list2 {ptr2.val}")
    #                 head.next = ptr2
    #                 ptr2 = ptr2.next
    #                 head = head.next
    #                # print(f"the current value of head is now {head.val}") 
    #     return mergelist.next
    
    
        head = ListNode(0, None)
        current = head
        
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
            
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        return head.next