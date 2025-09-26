class TrieNode(): 
    def __init__(self):
        self.children = {}
        self.finished = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word: 
            if char not in cur.children: 
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.finished = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word: 
            if char not in cur.children: 
                return False
            cur = cur.children[char]
        return cur.finished

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix: 
            if char not in cur.children: 
                return False
            cur = cur.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))      # True
