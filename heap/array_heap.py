import functools

@functools.total_ordering
class Node:
  def __init__(self, key, data):
    self.key = key
    self.data = data

  def __lt__(self, other):
    return self.key <= other.key

  def __eq__(self, other):
    return self.key == other.key

  def __str__(self):
    return "{(%d, %s)}" % (self.key, self.data)

class ArrayHeap:
  """
  Implementation of Heap using Array (List in this case)
  """
  def __init__(self, descending = True):
    self.list = []
    self.compare = lambda x, y: x > y if descending else lambda x, y: x < y 

  def add(self, key, data):
    node = Node(key, data)
    # add the new node to the end of the list
    self.list.append(node)
    # and trickle the last node up to right place
    self._trickle_up(self._last())

  def remove(self):

    if self.is_empty(): return None

    node = self.list[0]
    # move last node to the root
    last = self.list[-1]
    self.list[0] = last
    del self.list[-1]

    # trickle the new root down to proper place
    self._trickle_down(self._first())
    return node

  def is_empty(self):
    return len(self.list) == 0

  def _trickle_up(self, index):
  
    # keep going up the tree until we find right place which satisfies the heap condition (i.e. parent must be greater than it's children)
    while True:
      # parent is one level up divded by 2
      parent = (index - 1)/2
      if self._is_out_of_index(parent): break  # python lists can work with negative indexes, that's awesome but we don't want that here
    
      # if child is greater than the parent, then swap them
      #if self.compare(self.list[index], self.list[parent]):
      if self.list[index] > self.list[parent]:
        self.list[index], self.list[parent] = self.list[parent], self.list[index]
        index = parent
      else:
        break

  def _trickle_down(self, parent):

    # keep going down the tree until we find the right place which satisfies the heap condition (i.e. parent must be greater than the child)
    while True:
      # find the child with largest key 
      child = self._larger_child(parent)
      if not child: break
      
      # if child is greater than parent, then swap them 
      if self.list[child] > self.list[parent]:
        self.list[child], self.list[parent] = self.list[parent], self.list[child]
        parent = child
      else:
        break

  def _larger_child(self, parent):
    left, right = (2*parent + 1), (2*parent + 2)

    # heap is a complete tree, no right child can exist without left child
    # so if left child doesn't exist then just return
    if self._is_out_of_index(left):
      return None    

    # if right child doesn't exist, i.e only one child is there which is left child
    if self._is_out_of_index(right):
      return left

    # if both children are present, pick the bigger one
    return left if self.list[left] > self.list[right] else right

  def _is_out_of_index(self, index):
    if index < 0: return True
    if index > len(self.list) - 1: return True
    return False

  def _last(self):
    return len(self.list) - 1

  def _first(self):
    return 0

  def __str__(self):
    return "%s" % ["%d, %s" % (x[0], x[1]) for x in enumerate(self.list)]

def main():
  h = ArrayHeap(False)
  h.add(2, "Hello World 2")
  h.add(22, "Hello World 22")
  h.add(44, "Hello World 44")
  h.add(88, "Hello World 88")
  h.add(188, "Hello World 188")
  h.add(55, "Hello World 55")
  h.add(99, "Hello World 99")
  h.add(299, "Hello World 299")
  print "h : %s" % h
  print "removed : %s" % h.remove()
  print "removed : %s" % h.remove()
  print "h : %s" % h

if __name__ == "__main__":
  main()
