import random

# class stack():

#     def __init__(self, list = []) -> None:
#         self.list = list
#         print(self.list)
    
#     def add(self, n):
#         self.list.append(n)
#         return self.list
    
#     def remove(self):
#         self.list.pop()
#         return self.list
    
#     def insert(self, n, i):
#         self.list.insert(n, i)
#         return self.list
    
#     def lookup(self, n):
#         res = []
#         for i in range(len(self.list)):
#             if self.list[i] == n:
#                 res.append(i)
#         return res


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)

# dummy = ListNode()
# dummy.next = node1

# node1.next = node2
# node2.next = node3


head = ListNode(1)
dummy = ListNode()
node = ListNode()
node.next = head

for _ in range(2, 11):
    i = random.randrange(1, 50)
    head.next = ListNode(i)
    head = head.next

dummy.next = node

while node:
    print(node.val)
    node = node.next

print(dummy.next.val)