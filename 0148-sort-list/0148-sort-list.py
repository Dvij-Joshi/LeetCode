# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer=[]
        current=head
        while current:
            answer.append(current.val)
            current=current.next
        answer.sort()
        dummy=ListNode(0)
        dummy_head=dummy
        for num in answer:
            dummy.next=ListNode(num)
            dummy=dummy.next
        return dummy_head.next
        
