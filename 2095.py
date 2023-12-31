# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if head.next == None or head == None:
            return None

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = slow.next
        
        return head
        