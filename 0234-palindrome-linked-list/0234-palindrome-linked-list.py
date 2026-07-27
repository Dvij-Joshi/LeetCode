# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            curr = head

            while curr is not None:
                next_temp = curr.next  
                curr.next = prev      
                prev = curr           
                curr = next_temp    

            return prev 
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        p2=reverseList(slow)
        p1=head
        
        while p1 and p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next

        return True