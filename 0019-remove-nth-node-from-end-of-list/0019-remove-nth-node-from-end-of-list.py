# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        def lenlist(head):
            size = 0
            while head:
                size += 1
                head = head.next
            return size
        l = lenlist(head)
        temp = head
        if n == l:
            return temp.next
        for i in range(1,l):
            if i == l - n:
                temp.next = temp.next.next
                return head
            temp = temp.next

        return