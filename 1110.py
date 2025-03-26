from common import TreeNode, generateTree

def delNodes(root: TreeNode, to_delete: list[int]) -> list[TreeNode]:

    roots = [root]
    visited = set()
    q = [root]
    while len(q) != 0:
        node = q.pop()
        if node.val in to_delete:
            if node.left:
                roots.append(node.left)
            if node.right:
                roots.append(node.right)
            if node in roots:
                roots.remove(node)
        if node.left and node.left not in visited:
            visited.add(node.left)
            q.append(node.left)
            if node.left.val in to_delete:
                node.left = None

        if node.right and node.right not in visited:
            visited.add(node.right)
            q.append(node.right)
            if node.right.val in to_delete:
                node.right = None

    return roots



print(delNodes(generateTree([1,2,4, None, 3]), [3]))
