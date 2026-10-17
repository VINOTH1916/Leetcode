# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        finalist = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val)
                temp.next = node
                temp = temp.next
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                temp.next = node
                temp = temp.next
                list2 = list2.next
                
        while list1:
            node = ListNode(list1.val)
            temp.next = node
            temp = temp.next
            list1 = list1.next
        while list2:
            node = ListNode(list2.val)
            temp.next = node 
            temp = temp.next 
            list2 = list2.next
        
        return finalist.next
                
        
        
        
        