from queue import deque
import queue


class Node(object):
    def __init__(self, value, children=[]) -> None:
        self.value = value
        self.children = children

    def dfs(self):
        print(self.value, end='')
        for child in self.children:
            child.dfs()

    def postorder(self):
        for child in self.children:
            child.postorder()
        print(self.value, end='')

    def dfsIterative(self):
        stack = [self]
        while(len(stack)):
            node = stack.pop()
            print(node.value, end='')
            for child in node.children:
                stack.append(child)

    def bfsIterative(self):
        queue = deque([self])
        while(len(queue)):
            node = queue.popleft()
            print(node.value, end='')
            for child in node.children:
                queue.append(child)


#     a
#    / \
#   b   c
#  / \   \
# d   e   f
root = Node('a', [Node('b', [Node('d'), Node('e')]), Node('c', [Node('f')])])

root.dfs()

print("")

root.postorder()

print("")

root.dfsIterative()

print("")

root.bfsIterative()
