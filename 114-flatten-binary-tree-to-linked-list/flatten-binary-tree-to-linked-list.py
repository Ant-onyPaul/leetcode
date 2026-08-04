# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         self.prev=None
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.right)
#             dfs(node.left)
#             node.right=self.prev
#             node.left=None
#             self.prev=node
#         dfs(root)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def preorder(node):
            if not node:
                return

            nodes.append(node)      
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        # if nodes:
        #     nodes[-1].left = None
        #     nodes[-1].right = None