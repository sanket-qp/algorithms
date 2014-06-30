import random
from ..linkedlist import Node
from ..linkedlist import DoublyList
 
class LRU:
  """
  Implementation of LRU cache 
  LRU cache is implemented using python dictionary and Doubly Linked List 
  dictionary is used for look ups (i.e cache) and Doubly Linked List is used keeping track of recency of objects. 
  the objects which are used frequently are being kept near the head of the list and the ones which are not are kept towards the tail of the list

  Head of the List will always have most recetnly used object 
  Tail of the List will have least recently used object

  so whenever we need to purge any object from cache, we simply remove the one at the tail
  """
  def __init__(self, max_objects = 10):
    self.max = max_objects
    self.total = 0
    self.cache = {}
    self.list = DoublyList()

  def get(self, key):
    node = self.cache.get(key, None)
    if node: self.list.move_to_front(node)
    return node

  def put(self, key, data): 

    # check if already exist
    if key in self.cache:
      # just move this node to front of the list
      node = self.cache[key]
      self.list.move_to_front(node)
    # key doesn't exist, and cache is full
    elif self.total == self.max:
      self._remove_oldest()
      node = Node(key, data)      
      self.list.add_to_front(node)
      self.total += 1
    # key doesn't exist and cache is not full, then just add it and update the list
    else:
      node = Node(key, data)
      self.cache[key] = node
      self.list.add_to_front(node)
      self.total += 1

  def _remove_oldest(self):
    eldest = self.list.remove_last()
    # also remove this from the cache
    del self.cache[eldest.key]
    # decrement the count
    self.total -= 1

  def __str__(self):
    return "cache [%d] : %s \nreceny list :  %s" % (self.total, self.cache, self.list)

def main():
  n = 4
  cache = LRU(n)
  print "created a cache for storing %d objects" % n
  print "Adding (8, 'Object:8') to cache" 
  cache.put(8, 'Object:8')
  print "Cache : %s" % cache
  print "------"
  print "Adding (44, 'Object:44') to cache" 
  cache.put(44, 'Object:44')
  print "Cache : %s" % cache
  print "------"
  print "Adding (2, 'Object:2') to cache" 
  cache.put(2, 'Object:2')
  print "Cache : %s" % cache
  print "------"
  print "Adding (22, 'Object:22') to cache" 
  cache.put(22, 'Object:22')
  print "Cache : %s" % cache
  print "------"

  print "================"
  print "Cache is full, any new entries will remove the eldest object from the cache"
  print "================"
  print "Adding (4, 'Object:4') to cache" 
  cache.put(4, 'Object:4')
  print "Cache : %s" % cache
  print "------"
  
  print "Access to any object in the cache will update the recency list"
  o = cache.get(44)
  print "Accessed object with key 44, value : %s" % o
  print "Cache : %s" % cache
  print "------"

  print "and this how you can have an LRU which operates in constant time"

if __name__ == "__main__":
  main()
