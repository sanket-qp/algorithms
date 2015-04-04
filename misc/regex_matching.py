"""
Implement a function that return true if a string matches a passed in simple regex, the regex definition being:
'?' - matches any 1 char
'*' - matches 0 or more of any chars
'+' - matches 1 or more of any chars
                eg: For string - "abcdefgh", regex - "a?*e+h", result should be "true"
                
                abcd  abcd+ => true
                abcdef ab*cd => false
                abcdef ab*ef => true
                abcd ab+cd => false
"""
def matches(s, regex):
    #print s, regex
    # base cases
    if not s and not regex:
      return True

    if not regex:
      return True

    if not s:
      return False

    # recursive case
    # if first char matches, then move forward
    if s[0] == regex[0]:
      return matches(s[1:], regex[1:])
    elif regex[0] == '?':
      return matches(s[1:], regex[1:])
    elif regex[0] == '*':
      # try to match 0 or any characters, whenever there is a success, break and return True
      for i in range(0, len(s[1:])):
        if matches(s[1+i:], regex[1:]):
          return True
      return False
    elif regex[0] == '+':
      for i in range(1, len(s)):
        if matches(s[i:], regex[1:]):
          return True
      return False
    else: 
      return False

def main():
  testCases = [("abcd", "abcd"), 
                ("abcd", "*"), 
                ("xyz", "abc"), 
                ("abccccccccccd", "a?*d"), 
                ("abccccccd", "a?*f"),
                ("abcd", "ab+cd"),
                ("abccccceef", "ab+d"),
                ("abcd", "abcd+"),
                ("xyzabc", "xy+c"),
              ]
  for s, regex in testCases:
    print "matches('%s', '%s') = %s" % (s, regex, matches(s, regex))

if __name__ == "__main__":
  main()
