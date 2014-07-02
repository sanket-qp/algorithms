import random

def merge(a, b):
  c = []
  ia = ib = 0
  while ia < len(a) and ib < len(b):
    if a[ia] < b[ib]:
      c.append(a[ia])
      ia += 1
    else:
      c.append(b[ib])
      ib += 1

  # check if any of the original list still has elements
  while ia < len(a):
    c.append(a[ia])
    ia += 1
  
  while ib < len(b):
    c.append(b[ib])
    ib += 1
  
  return c

def sort(l):
 
  # base case when list of only one element
  if not l or len(l) <= 1:
    return l

  # split the list in two
  mid = len(l)/2
  # merge the result of two sorted sublists
  return merge(sort(l[:mid]), sort(l[mid:]))

def main():
  n = 10
  l = [random.randint(0, 100) for _ in range(n)] 
  print "before sorting : %s" % l
  l = sort(l)
  print "after sorting  : %s" % l
  pass

if __name__ == "__main__":
  main()
