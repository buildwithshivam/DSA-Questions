class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_sum = 0
            length = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_sum / length)

        return result
