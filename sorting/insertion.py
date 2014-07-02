import random

def sort(l):
  """
  implementation of insertion sort
  """
  for i in range(len(l)):
    # mark the element
    marked = l[i]
    j = i
    # keep looking and shifting elements to the right until you find the element which is smaller than marked 
    while j > 0 and marked < l[j - 1]:
      # shift right
      l[j] = l[j - 1]
      j = j -1
    # place marked element at the correct spot
    l[j] = marked  

def main():
  n = 10
  l = [random.randint(0, 100) for _ in range(n)] 
  print "before sorting : %s" % l
  sort(l)
  print "after sorting  : %s" % l

if __name__ == "__main__":
  main()
