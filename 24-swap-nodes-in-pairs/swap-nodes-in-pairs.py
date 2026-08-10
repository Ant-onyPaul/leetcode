# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         arr=[]
#         curr=head
#         while curr:
#             arr.append(curr.val)
#             curr=curr.next
#         n=len(arr)
#         if n%2==0:
#             left=0
#             right=1
#             while right<=n-1:
#                 arr[left],arr[right]=arr[right],arr[left]
#                 left+=2
#                 right+=2
#         else:
#             left=0
#             right=1
#             while right<n:
#                 arr[left],arr[right]=arr[right],arr[left]
#                 left+=2
#                 right+=2
#         dummy=ListNode()
#         tail=dummy
#         for i in arr:
#             tail.next=ListNode(i)
#             tail=tail.next
#         tail.next=None
#         return dummy.next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next and curr.next.next:

            first = curr.next
            second = curr.next.next

            first.next = second.next
            second.next = first
            curr.next = second

            curr = first

        return dummy.next