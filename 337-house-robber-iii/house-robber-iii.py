# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rob(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return []
#         ans=[]
#         q=[root]
#         while q:
#             level=[]
#             for i in range(len(q)):
#                 node=q.pop(0)
#                 level.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             ans.append(level)
#         res=[]
#         for i in ans:
#             for j in i:
#                 res.append(j)
#         prev1=0
#         prev2=0
#         curr=0
#         for i in range(len(res)):
#             curr=max(prev1,prev2+res[i])
#             prev2=prev1
#             prev1=curr
#         return curr
class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current node
            rob = node.val + left[1] + right[1]

            # Don't rob current node
            not_rob = max(left) + max(right)

            return [rob, not_rob]

        ans = dfs(root)

        return max(ans)