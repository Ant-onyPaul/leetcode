# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        rootval=preorder.pop(0)
        root=TreeNode(rootval)
        mid=inorder.index(rootval)
        root.left=self.buildTree(preorder,inorder[:mid])
        root.right=self.buildTree(preorder,inorder[mid+1:])
        return root