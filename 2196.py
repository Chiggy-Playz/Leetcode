from common import TreeNode

def createBinaryTree(descriptions: list[list[int]]) -> TreeNode:
    # val: tree node
    nodes = {}
    children = set()

    for parent, child, isLeft in descriptions:
        if child not in nodes:
            nodes[child] = TreeNode(child, None, None)

        if parent not in nodes:
            nodes[parent] = TreeNode(
                parent,
                nodes[child] if isLeft else None,
                None if isLeft else nodes[child],
            )
        else:
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        children.add(child)

    return nodes[(set(nodes.keys()).difference(children)).pop()]


root = createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])

to_visit = [root]
while len(to_visit) != 0:
    node = to_visit.pop(0)
    if node.left:
        print(node.left)
        to_visit.append(node.left)

    if node.right:
        to_visit.append(node.right)
        print(node.right)
