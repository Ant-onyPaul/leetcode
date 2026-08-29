# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        og=[]
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            og.append(node.val)
            dfs(node.right)
        dfs(root)
        og.append(val)
        def dfs(arr):
            if not arr:
                return None
            maxx=max(arr)
            ind=arr.index(maxx)
            root=TreeNode(maxx)
            root.left=dfs(arr[:ind])
            root.right=dfs(arr[ind+1:])
            return root
        return dfs(og)