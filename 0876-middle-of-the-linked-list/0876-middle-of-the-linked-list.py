# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        fast=head
        slow=head
        while current:
            if fast==None:
                return slow
            else:
                if fast.next:
                    if fast.next.next:
                        fast=fast.next.next
                        slow=slow.next
                    else:
                        # slow = slow.next
                        return slow.next
                else:
                    return slow
            