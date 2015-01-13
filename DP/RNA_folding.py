"""
finding secondary substrucutre in RNA using recursion and dynamic programming
here is a very nice lecture discussing this problem, https://www.youtube.com/watch?v=h60raqnvm0s
"""
def matches(chA, chB):
  if chA == 'A' and chB == 'U':
    return True

  if chA == 'U' and chB == 'A':
    return True

  if chA == 'C' and chB == 'G':
    return True

  if chA == 'G' and chB == 'C':
    return True

  return False

def opt_dp(rna_string, i, j):
  pass

# here is the recursive solution
def opt(rna_string, i, j):
  print "%d, %d" % (i, j)
  # base case
  # both chracters can't be considered if they are closer than 4 steps
  if i < 0:
    return 0

  if j < 0:
    return 0

  if (j-i) <= 4: 
    return 0

  if i > j:
    return 0

  if not matches(rna_string[i], rna_string[j]):
    return 0

  # recursive case
  # we want to come up with a recurrence such that opt (i, j) can be solved using the sub problems
  # one way to think about it is, what are the options for a character at position j
  # option 1, j is not used in the secondary substructure, so we'll find solutions of i to j-1, i.e. opt(i, j-1)
  option1 = opt(rna_string, i, j-1)

  # option 2, j is included in the secondary substructure
  # let say, j is paird with some character at place t, but t could be any character betweet i and j, 
  # so we have to try to match all the characters between i and j which can be matched with j 
  
  options = []
  for t in range(i, j-4):
    """
    temp = 1 + opt(i, t-1) # once j is matched with t, we have two other options, i to t-1 AND t+1, j-1 
             + opt(t+1, j-1) 
    """
    temp = 1 + opt(rna_string, i, t-1) + opt(rna_string, t+1, j-1)
    options.append(temp)

  option2 = max(options)
  return max(option1, option2)

def main():
  print matches('U', 'A')
  rna = 'AUGUUACGGGGCCAACAU'
  rna = 'ACGAUXXXXAUCGU'
  print "%d" % opt(rna, 0, len(rna)-1)

if __name__ == "__main__":
  main()
