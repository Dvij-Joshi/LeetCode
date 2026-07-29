# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        if not head or not head.next:
            return head
        current=head
        n=0
        tail=None
        while current:
        
            n += 1
            if current.next is None:
                tail = current
            current = current.next
        k=k%n
        if k==0:
            return head
        i=0
        current=head
        while i<(n-k-1):
            current=current.next
            i+=1
        new_head=current.next
        tail.next=head
        head=new_head
        current.next=None
        return head


            
        

        