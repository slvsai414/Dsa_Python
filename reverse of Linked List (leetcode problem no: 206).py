# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        temp = head
        while temp is not None:
            front = temp.next
            temp.next = rev
            rev = temp
            temp = front
        return rev
