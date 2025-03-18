# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = 0; t = head
        while(t.next): d += 1;  t = t.next

        mom = int(d/2) + (1 if d%2 != 0 else 0)
        res = head
        for _ in range(mom): res = res.next
        return res
