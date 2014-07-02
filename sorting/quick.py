import random
"""
Implementation of Quicksort
TODO:: add verbose flag and log thouroughly so it's easy to debug
"""
def partition(l, left, right):
  """
  this partitioning function is core of quicksort 
  all it does is partitons the array in a way that all elements left to the pivot are smaller than pivot and elements on the right are bigger than pivot
  """
  left_scans = 0
  right_scans = 0
  pivot_index = left # pivot is the first element 
  pivot = l[pivot_index]

  # set up left and right pointers
  left_ptr = left 
  right_ptr = right - 1

  # keep looking until we find the right place to move the pivot
  while True:
    # keep going from left to right until the elements are less than pivot
    # in other words ,find the first element which is greater than pivot
    while (left_ptr < right and l[left_ptr] <= pivot):
      left_ptr += 1 
      left_scans += 1 
  

    # keep going from right to left until we find the element which is less than pivot
    while (right_ptr > left and l[right_ptr] > pivot):
      right_ptr -= 1
      right_scans += 1

    # we have found the indexes in the list where one element is greater than the pivot (on the left side of the array) 
    # while other one is less than the pivot (right side of the array)

    # check if we have covered the whole array or there are elements left to inspect
    if (right_ptr <= left_ptr):
      # we are done, pointers have crossed each other
      break
    else:
      # swap the elements and keep looking
      # i.e, put the element greater than the pivot towards the right side of array, 
      # and put the element less than the pivot towards the left side of the array
      # this swap operation will give us array with the elements less than pivot on the left side
      # and elements greater than pivot on the right side
      l[left_ptr], l[right_ptr] = l[right_ptr], l[left_ptr]
  
  partition = left_ptr - 1  
  # move pivot to parition
  l[pivot_index], l[partition] = l[partition], l[pivot_index]
  # we come here when pointers crossed each other, i.e. left_ptr was the last spot where we couldn't go any further
  # we'll take this as a paritioning spot, all the elements left of this SPOT (index in array) will be less than pivot and all elements right to this SPOT 
  # will be greater than the pivot 
  print "left scans : %d [%d], right scans : %d [%d]" % (left_scans, left_ptr, right_scans, right_ptr)
  print l
  return partition

def sort(l, left, right):
  
  # Base case
  if right <= left:
    return

  split = partition(l, left, right)
  # do the same process for left subarray [0 to split]
  sort(l, left, split)
  # same thing for right subarray [split+1, len(l)]
  sort(l, split+1, right)

def main():
  n = 10
  # list of integers
  l = [random.randint(0, 100) for _ in range(n)] 
  l = [10, 9, 8, 7, 6, 5, 4]
  l = [1, 2, 3, 4, 5, 6, 7, 8]
  print "before sorting : %s" % l
  sort(l, 0, len(l))
  print "after sorting  : %s" % l

if __name__ == "__main__":
  main()
