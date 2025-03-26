from common import TreeNode, getTree1


def getDirections(root: TreeNode, startValue: int, destValue: int):
    parents = {}
    node1 = node2 = None
    stack = [root]
    visited = set()

    while len(stack) != 0:
        current_node = stack.pop()

        if current_node.val in (startValue, destValue):
            if current_node.val == startValue:
                node1 = current_node
            else:
                node2 = current_node

            if node1 and node2:
                break

        if current_node.left and current_node.left not in visited:
            visited.add(current_node.left)
            stack.append(current_node.left)
            parents[current_node.left] = current_node

        if current_node.right and current_node.right not in visited:
            visited.add(current_node.right)
            stack.append(current_node.right)
            parents[current_node.right] = current_node

    assert node1 and node2

    path1 = getPath(parents, node1, root)
    # Reverse the second path
    path2 = getPath(parents, node2, root)

    i = len(path1) - 1
    j = len(path2) - 1

    while True:
        if i == 0 or j == 0:
            break

        if path1[i - 1] == path2[j - 1]:
            i -= 1
            j -= 1
        else:
            break

    # i+1 because we want to include the common element
    path = path1[: i + 1] + path2[:j][::-1]
    result = ""

    for n1, n2 in zip(path[:-1], path[1:]):
        if n2 == n1.left:
            result += "L"
        elif n2 == n1.right:
            result += "R"
        else:
            result += "U"

    return result


# node1: start
# node2: end
def getPath(parents: dict[TreeNode, TreeNode], node1: TreeNode, node2: TreeNode):
    path = [node1]
    current_node = node1
    while current_node != node2:
        current_node = parents[current_node]
        path.append(current_node)

    return path

START = 3
DEST = 6

print(getDirections(getTree1(), START, DEST))
