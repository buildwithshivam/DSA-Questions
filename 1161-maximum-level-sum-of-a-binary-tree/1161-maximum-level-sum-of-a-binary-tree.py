from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        answer_level = 1
        max_sum = root.val

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level

            level += 1

        return answer_level