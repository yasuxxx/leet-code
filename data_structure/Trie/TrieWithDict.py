import operator
from functools import cmp_to_key


class Trie:
    def __init__(self):
        # 每个子树都是一个字典（包含二十六个字母）
        self.root = {}
        self.end = -1

    def insert(self,word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = {}

    def search(self,word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return self.end in curNode

    def startWith(self,word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True

if __name__ == '__main__':
    # trie = Trie()
    # trie.insert('apa')
    # trie.insert('apb')
    # trie.insert('apple')
    # print(trie.search('app'))
    # print(trie.search('apa'))
    # print(trie.search('apb'))
    # print(trie.search('apple'))
    # print(trie.startWith('app'))
    # print(trie.startWith('apa'))
    # print(trie.startWith('apb'))
    # print(trie.startWith('apple'))
   test = ['a','aaa','abcd','aa','d','c','b']
    #  sort原地修改   sorted修改后返回
    # 字符串的自定义比较方法：key 传入 cmp_to-key
    # 字符串的字典序比较方法：operator.lt
   def compare(x,y):
        if len(x)==len(y):
            return -1 if operator.lt(x,y) else 1
        else:
            return len(y)-len(x)
   res = sorted(test,key=cmp_to_key(lambda x,y:compare(x,y)))
   # print(test)
   print(res)
