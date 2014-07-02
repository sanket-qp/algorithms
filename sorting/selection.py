import random

def sort(l):
  """
  Implementation of selection sort
  """
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if l[j] < l[i]:
        # because Python rules :)
        l[i], l[j] = l[j], l[i]

def recursive_sort(l, index = 0):
  """
  recursive version
  """
  # base case, if we are at the last element
  if index == len(l) - 1:
    return 

  # compare the element at index with other elements and swap if necessary
  for j in range(index+1, len(l)):
    if l[j] < l[index]:
      l[j], l[index] = l[index], l[j]

  # shrink the list by one element and do the same thing recursively for the sublist (index+1)
  recursive_sort(l, index+1)

def main():
  n = 10
  l = [random.randint(0, 100) for _ in range(n)] 
  print "before sorting : %s" % l
  sort(l)
  print "after sorting  : %s" % l

if __name__ == "__main__":
  main()
