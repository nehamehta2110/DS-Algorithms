"""
Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.eof = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root_node = self.root
        for i in list(word):

            if not root_node.children.get(i):
                root_node.children[i] = TrieNode()
            root_node = root_node.children[i]

        root_node.eof = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root_node = self.root
        for i in list(word):
            if not root_node.children.get(i):
                return False
            root_node = root_node.children[i]

        return root_node.eof and root_node is not None

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root_node = self.root
        for i in list(prefix):
            if not root_node.children.get(i):
                return False
            root_node = root_node.children[i]

        return root_node is not None


def main():
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))


if __name__ == '__main__':
    main()
