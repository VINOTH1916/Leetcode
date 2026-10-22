class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        fast = head
        slow = head
        head1 = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast =  fast.next.next
        
       
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head2 = prev

        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2




        