

class Trie:
    def __init__(self):
        # 每个子树都是一个长度为27的数组（索引0-25表示对应的二十六个字母）
        # 26表示是否是边界
        self.root = [None]*27

    def insert(self,word):
        curNode = self.root
        for c in word:
            ind = ord(c)-ord('a')
            if not curNode[ind]:
                curNode[ind] = [None]*27
            curNode = curNode[ind]
        curNode[26] = 1

    def search(self,word):
        curNode = self.root
        for c in word:
            ind = ord(c)-ord('a')
            if not curNode[ind]:
                return False
            curNode = curNode[ind]
        return curNode[26]==1

    def startWith(self,word):
        curNode = self.root
        for c in word:
            ind = ord(c)-ord('a')
            if not curNode:
                return False
            curNode = curNode[ind]
        return True
if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.insert('app')
    trie.insert('acde')
    trie.insert('ace')
    trie.insert('acfg')
    trie.insert('bce')

    print(trie.search('app'))
    print(trie.search('appl'))
    print(trie.search('apple'))
    print(trie.search('acd'))
    print(trie.search('ac'))
    print(trie)

