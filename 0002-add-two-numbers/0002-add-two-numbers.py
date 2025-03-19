# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # 더미 노드 생성
        cur = dummy_head  # 현재 위치 포인터
        carry = 0  # 올림수 초기화

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry

            carry = total // 10  # 10 이상의 값이면 올림 발생
            cur.next = ListNode(total % 10)  # 한 자리 숫자만 저장
            cur = cur.next  # 다음 노드로 이동

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next  # 첫 번째 노드 반환