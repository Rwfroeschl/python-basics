
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    """
    children dictionary to map it's next potential characters to child nodes
    endOfWord tracks whether it represents the end of a word 
    """
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True

    """
    this method above, loops through each character in the word we want to insert.
    at each step, it checks if the next child node for the character exists in the
    current node's children map. if child does not exist, create a new TrieNode with
    that character. Current node progresses to the new child node and loop continues.
    endOfWord is marked at the end of loop to help establish the end of the word
    """
    
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfWord
    
    """
    traverse through the characters of the word to check, grabbing child nodes from 
    the current node's children map. if a child node does not exist for the next character
    then we know the word cannot exist, so return False. Otherwise, we reach the end of
    the word and return if the current char is a endOfWord.
    """

    def remove(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                raise Exception("word isn't here")
            current = current.children[char]
        current.endOfWord = False
        # remove any children from the node that were left behind
        if current.children == {}:
            parent = self.__find_parent(current)
            del parent.children[char]
    
    """
    We traverse to the end of the word (if it exists) and set the endofword to false.
    We then remove all children of the node that are not being used
    """


bundle = Trie()
bundle.add_word("something")
bundle.add_word("slippery")
bundle.add_word("some")
bundle.add_word("soup")

bundle.remove("some")
bundle.exists("some")
# should return false
