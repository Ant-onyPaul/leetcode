# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return None
            node=max(arr)
            ind=arr.index(node)
            root=TreeNode(node)
            root.left=dfs(arr[:ind])
            root.right=dfs(arr[ind+1:])
            return root
            
        return dfs(nums)