class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(node):
            if node.left:
                inorder(node.left)
            ans.append(node.val)
            if node.right:
                inorder(node.right)
        if root:
            inorder(root)
        return ans