# arr = list(map(int, open('day20/tc.txt').read().split('\n')))
arr = list(map(int, open('day20/input.txt').read().split('\n')))

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  
  def __str__(self):
    return str(self.value)

class DoublyCircularLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def append(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
      node.next = node
      node.prev = node
    else:
      node.next = self.head
      node.prev = self.tail
      self.head.prev = node
      self.tail.next = node
      self.tail = node
    self.size += 1
    return node
  
  def remove(self, node):
    if self.size == 1:
      self.head = None
      self.tail = None
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      if node == self.head:
        self.head = node.next
      if node == self.tail:
        self.tail = node.prev
    self.size -= 1
  
  def at_after(self, node, steps):
    curr = node
    for _ in range(steps % self.size):
      curr = curr.next
    return curr
  
  def insert(self, node, new_node):
    new_node.prev = node
    new_node.next = node.next
    node.next.prev = new_node
    node.next = new_node
    self.size += 1
  
  def move_node(self, node, steps):
    curr = node.prev
    self.remove(node)
    if steps > 0:
      for _ in range(steps):
        curr = curr.next
    else:
      for _ in range(-steps):
        curr = curr.prev
    self.insert(curr, node)
  
  def __str__(self):
    node = self.head
    arr = []
    for _ in range(self.size):
      arr.append(str(node))
      node = node.next
    return ' '.join(arr)

a = DoublyCircularLinkedList()
nodes = []
zero = None
for x in arr:
  node = a.append(x)
  nodes.append(node)
  if x == 0:
    zero = node

for node in nodes:
  a.move_node(node, node.value)

print(a.at_after(zero, 1000).value + a.at_after(zero, 2000).value + a.at_after(zero, 3000).value)
