# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans=[]
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            ans.append(node)
            dfs(node.right)
        dfs(root)
        first=None
        second=None
        for i in range(len(ans)-1):
            if ans[i].val>ans[i+1].val:
                if first is None:
                    first=ans[i]
                second = ans[i+1]
        first.val,second.val=second.val,first.val
        
