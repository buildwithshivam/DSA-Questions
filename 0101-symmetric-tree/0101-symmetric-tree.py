class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        pairs = [(root.left,root.right)]
        i = 0

        while i < len(pairs):
            a,b = pairs[i]
            i += 1

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            pairs.append((a.left,b.right))
            pairs.append((a.right,b.left))
            
        return True