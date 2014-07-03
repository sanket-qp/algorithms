import functools

@functools.total_ordering
class Node:
  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.left = None
    self.right = None
    self.parent =  None

  def __lt__(self, other):
    return self.key <= other.key

  def __eq__(self, other):
    return self.key == other.key

  def __str__(self):
    return "{(%d, %s)}" % (self.key, self.data)

class TreeHeap:
  """
  Implementation of heap using binary tree
  """
  
  def __init__(self):
    self.root = None
    self.total = 0

  def add(self, key, data): 
    """
    adds an element to the heap
    """
    node = Node(key, data)
    if not self.root:
      self.root = node
    else:
      # total+1 will give us the first null node, where we want to add the new node
      path = self._get_path(self.total + 1)
      parent = current = self.root
      is_left_child = True

      while(current and path):
        direction = path.pop(0)
        parent = current
        if direction == 1:
          current = current.right
          is_left_child = False
        else:
          current = current.left
          is_left_child = True

      # found a node
      if is_left_child: parent.left = node
      else: parent.right = node
      node.parent = parent
      # after a node is added to the end, trickle it up
      self._trickle_up(node)

    self.total += 1

  def remove(self):
    """
    removes the root element of the heap
    """
    if not self.root:
      return None
    
    node = Node(self.root.key, self.root.data)
    # move the last node to root, total is the last node
    path = self._get_path(self.total)
    current = self.root
    is_left_child = True
    while (current and path):
      direction = path.pop(0)
      parent = current
      if direction == 1:
        current = current.right
        is_left_child = False
      else:
        current = current.left
        is_left_child = True

    bottom = parent.left if is_left_child else parent.right
    # detach bottom from it's parent
    if is_left_child: 
      parent.left = None
    else:
      parent.right = None

    # swap contents of root and bottom
    self._swap_contents(bottom, self.root)
    # trickle it down
    self._trickle_down(self.root)
    self.total -= 1
    return node

  def _trickle_up(self, node):
    """
    trickles the node up to a place where heap condition is satisfied
    """
    current = node
    while True:
      parent = current.parent
      if not parent: break
      if current > parent:
        self._swap_contents(current, parent)
        current = parent
      else:
        break
  
  def _trickle_down(self, node):
    """
    trickles the node down to a place where heap condition is satisfied
    """
    parent = node
    while True:
      child = self._larger_child(parent)
      if not child: break

      if child > parent:
        self._swap_contents(child, parent)
        parent = child
      else:
        break
      
  def _larger_child(self, node):
    """
    returns the larger child of a node
    """
    if not node.left:
      return None
    
    if not node.right:
      return node.left

    return node.left if node.left > node.right else node.right

  def _get_path(self, n):
    # binary representation of n which gives the path to nth node
    # 1 indicates take the right child and 0 indicates taking left child
    # 6th node (binary 10 after disarding first bit of 110) can be reached by traversing right (1), and then left (0) from the root node 
    path = []
    while n >= 1:
      path.append(n % 2)
      n = n/2

    path.reverse()
    # we don't really need first bit
    return path[1:]

  def _swap_contents(self, frm, to):
    """ 
    swaps contents (key and data) of two nodes
    """
    temp = Node(to.key, to.data)
    to.key = frm.key
    to.data = frm.data
    frm.key = temp.key
    frm.data = temp.data
    
  def __str__(self):
    """
    bfs traversal 
    """
    nodes = []
    counter = 1
    queue = []
    queue.append(self.root)
    while queue:
      current = queue.pop(0)
      nodes.append("[%d, %s]" % (counter, current))
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
      counter += 1

    return " ".join(nodes)

def main():
  h = TreeHeap()
  print "Adding some data to heap"
  h.add(2, "Hello World 2")
  h.add(22, "Hello World 22")
  h.add(44, "Hello World 44")
  h.add(88, "Hello World 88")
  h.add(188, "Hello World 188")
  h.add(55, "Hello World 55")
  h.add(99, "Hello World 99")
  h.add(299, "Hello World 299")
  print "After adding : %s" % h
  print "----------------"
  print "removed : %s" % h.remove()
  print "removed : %s" % h.remove()
  print "After removing : %s" % h
  print "----------------"
  print "Adding some data again"
  h.add(299, "Hello World 299")
  h.add(2, "Hello World 2")
  print "After adding : %s" % h

if __name__ == "__main__":
  main()
