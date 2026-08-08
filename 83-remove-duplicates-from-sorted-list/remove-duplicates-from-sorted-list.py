# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        arr=[]
        real=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        n=len(arr)
        for i in range(n-1):
            if arr[i]!=arr[i+1]:
                real.append(arr[i])
        if arr:
           real.append(arr[-1])
        dummy=ListNode()
        tail=dummy
        for i in real:
            tail.next=ListNode(i)
            tail=tail.next
        tail.next=None
        return dummy.next
