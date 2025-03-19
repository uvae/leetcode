# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s: Optional[ListNode] = None
        l: Optional[ListNode] = None
        c = False

        while(l1 or l2 or c):
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + (1 if c else 0)
            if(s):
                l.next = ListNode(v%10, None)
                l = l.next
            else:
                s = ListNode(v%10, next=None)
                l = s
            
            c = True if v >= 10 else False
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
        
        return s