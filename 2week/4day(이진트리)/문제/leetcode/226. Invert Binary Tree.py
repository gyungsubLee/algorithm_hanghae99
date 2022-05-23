# 문제)

# 풀이1) 파이썬 다운 방식
import collections


def invertTree(self, root:TreeNode) -> TreeNode:
    if root:
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None

# 풀이2) BFS
def inverTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        #부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root

# 풀이3) DFS
def inverTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

    return root