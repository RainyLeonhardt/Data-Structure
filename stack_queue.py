from matplotlib import collections
from queue import deque

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack[0])
print(stack[-1])
print(stack.pop())

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q[0])
print(q[-1])
print(q.popleft())

# deque1 = collections.deque("abcdefg")
# print("deque:", deque1)
# print("Length:", deque1)
# print("left_end:", deque1[0])
# print("reight_end:", deque1[-1])

# deque1.remove("c")
# print("remove(c):", deque1)
