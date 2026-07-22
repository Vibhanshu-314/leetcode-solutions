# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # phle middle elemnt nikala  jiissee hum do alag alg ll bna skeee
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # disconnect the half ll
        second=slow.next
        slow.next=None

        # abb hum second wali ko reverse kr rhe hai 

        prev=None
        curr=second

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt


        # merge bhi toh krna hai 


        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
            