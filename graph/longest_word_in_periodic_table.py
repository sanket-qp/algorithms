"""
find the longest word that can be formed from periodic table

we'll build a complete graph of given words (i.e. each word is connected to every other word)
then we'll do DFS on each word and check the dictionary if that path forms a word or not
"""
def prepare_dictionary(word_file):
    """
    prepares a dictionary and prefixes of all dictionary words
    """
    d = set()
    prefixes = set()
    for word in open(word_file):
        word = word.strip()
        d.add(word)
        # lets also store all prefixes of this word
        # this will let us search faster
        for i in range(1, len(word) + 1):
            prefixes.add(word[:i])

    return d, prefixes

def neighbors(index, words):
    """
    returns neighbors of word at given index
    as this is a complete graph, every other word is a neighbor of given word
    """
    for j in range(len(words)):
        if j != index:
            yield j 

def DFS(node, p_table, path, english_dict, prefixes, longest_word):
    # check if path so far forms a word or is a prefix of a word
    word_so_far = ''.join(p_table[i].lower() for i in path)

    # if current path doesn't lead to a valid word then don't explore further
    if word_so_far not in prefixes:
        return 

    if word_so_far in english_dict:
        current_longest = longest_word.get('longest', '')
        if len(word_so_far) > len(current_longest):
            # don't use lowercase version
            _word = ''.join(p_table[i] for i in path)
            longest_word['longest'] = _word
    
    for neighbor in neighbors(node, p_table):
        # we only want to visit neighbors which are not in progress
        if neighbor not in path:
            DFS(neighbor, p_table, path+[neighbor], english_dict, prefixes, longest_word)

def longest_word(periodic_table, english_dict, prefixes):
    longest_word = {}
    for index, word in enumerate(periodic_table):
        DFS(index, periodic_table, [index], english_dict, prefixes, longest_word)

    return longest_word.get('longest', None)

def main():
    english_dict, prefixes = prepare_dictionary('words_all.txt')
    # small table for testing 
    #periodic_table = ['li', 'cu', 'he', 'o', 'll', 'ab', 'e', 's', 'a']
    
    # complete table 
    periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V',
                      'Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru',
                      'Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb',
                      'Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
                      'Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh',
                      'Hs','Mt','Ds','Rg','Cn','Uut','Uuq','Uup','Uuh','Uus','Uuo']

    # small sample of the whole table 
    """
    periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V',
                      'Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru',
                      'Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb']
    """
    longest = longest_word(periodic_table, english_dict, prefixes)
    print "longest_word: %s of length: %d" % (longest, len(longest))

if __name__ == "__main__":
    main()
