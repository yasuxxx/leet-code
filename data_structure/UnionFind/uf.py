from collections import defaultdict


class UF:
    def __init__(self,n):
        self.parent = defaultdict(int)
        self.count = n
        for i in range(n):
            self.parent[i] = i

    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP!=rootQ:
            self.parent[rootP] = rootQ
            self.count-=1

    def connected(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootQ==rootP

    def find(self,x):
        while(x!=self.parent[x]):
            self.parent[x] = self.parent[self.parent[x]]
            x =self.parent[x]
        return x

if __name__ == '__main__':
     uf  = UF(7)
     uf.union(0,1)
     uf.union(0, 6)
     uf.union(0,3)
     uf.union(0, 2)
     uf.union(2,5)
     print(uf.connected(0, 5))
     print(uf.connected(4, 5))