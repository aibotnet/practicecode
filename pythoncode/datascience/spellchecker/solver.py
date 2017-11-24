import sys
from collections import defaultdict



class Node(object):
    def __init__(self):
        self.next = defaultdict(int)


#create trie data structure from all words in dictionary
class Trie(object):
    def __init__(self, inFile):
        self.nodes = []
        self.nodes.append(Node())
        self.n = 1

        for line in open(inFile, 'r'):
            currNode = 0
            for char in line.split('\n')[0]:
                if self.nodes[currNode].next[char] == 0:#if charecter is not present
                    self.nodes.append(Node())
                    self.nodes[currNode].next[char] = self.n
                    currNode = self.n
                    self.n += 1
                else:
                    currNode = self.nodes[currNode].next[char]#charecter is already present


    #find word is present in trie or not
    def find(self, word):
        """Return the frequency of the given word."""
        currNode = 0
        for char in word:
            if self.nodes[currNode].next[char] == 0:
                return
            else:
                currNode = self.nodes[currNode].next[char]
        print word


def stringOf(cl):
    s = ''
    for i in cl:
        s+=i
    return s


def swap(cl, i, j):
    temp = cl[i]
    cl[i] = cl[j]
    cl[j] = temp


def allPermutations(trie, charList, i, n):#generate all permutation
    if i == n:
        trie.find(stringOf(charList))
    else:
        for j in range(i, n+1):
            swap(charList, i, j)
            allPermutations(trie, charList, i+1, n)
            swap(charList, i, j)



if __name__ == '__main__':
    word = sys.argv[1]
    trie = Trie('dictionary .txt')
    allPermutations(trie, list(word),0,len(word)-1)
