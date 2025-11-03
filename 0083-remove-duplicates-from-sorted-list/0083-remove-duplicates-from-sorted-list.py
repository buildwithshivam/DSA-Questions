# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        seen = set()
        seen.add(head.val)
        cur = head 
        while cur.next:
            seen.add(cur.val)
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                seen.add(cur.next.val)
                cur = cur.next
        return head 