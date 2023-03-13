from collections import deque


class recursion_practice(object):
    
    def __init__(self) -> None:
        self.s = 0

    def factorial(self, n):
        if n > 0:
            return n * recursion_practice.factorial(n - 1)
        else:
            return 1
    
    def factorial_iterative(n):
        s = 1
        while n > 1:   
            s *= n
            n -= 1
        return s

    def Fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return recursion_practice.Fibonacci(n - 1) + recursion_practice.Fibonacci(n - 2)
        

# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

# print(recursion_practice.Fibonacci(7))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dep(root, path):
        if not root:
            return
        path += 1
        Node.dep(root.left, path + 1)
        Node.dep(root.right, path + 1)
        return path
    
    def findsum(root, pathsum, target):
        if not root:
            return
        if pathsum == target:
            return True
        Node.findsum(root.left, pathsum + root.val, target)
        Node.findsum(root.right, pathsum + root.val, target)
    def bfs(root):
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

    def bfs_child(root):
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                for c in curr.children:
                    queue.append(c)
            level += 1
        return level

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.left.right = Node(9)
path = 0
pathsum = 0
target = 24
mp = []

# print(Node.maxDepth(root))
# print(Node.findsum(root, pathsum, target))



# print(Node.bfs(root))

class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def bfs(root):
        level = 0
        r = []
        res = []
        if not root:
            return -1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                cand = q.popleft()
                r.append(cand.val)
                # print(r)
                if cand.left:
                    q.append(cand.left)
                if cand.right:
                    q.append(cand.right)
            res.append(r)
            r = []
            level += 1
        return res, level

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.left.left.left = TreeNode(88)
root1.right.right.right = TreeNode(8)

print(TreeNode.bfs(root1))