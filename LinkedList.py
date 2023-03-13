class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __str__(self) -> str:
        cur = self
        output = ""
        while cur:
            output += str(cur.value)
            cur = cur.next
        return output

def list2linkedlist(nums):
    head = None
    cur = None
    for n in nums:
        Node(n)
        if not head:
            head = Node(n)
            cur = head
        else:
            cur = Node(n)
            cur = cur.next
    return head

# class LinkedList(object):
#     def __init__(self, node):
#         self.head = node

n = Node(1, Node(2, Node(3)))
print(n)

# print(list([10,20,30]))
nums = [1,2,3,4,5,6]
print(list2linkedlist(nums))