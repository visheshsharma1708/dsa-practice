from lc2 import ListNode


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the kth node of the current group
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the current group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp