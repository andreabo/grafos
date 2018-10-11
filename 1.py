class Graph(object):
    def __init__(self, n):
        self.g = {}
        self.n = n
        
        for i in range(n):
            self.g[i] = []
            
    def addEdge(self, n1, n2, w):
        self.g[n1].append((n2, w))
    

    def shortestPathHelper(self, n1, n2, visited, totalValue, path):
        visited[n1] = True    
        t = totalValue
        r = []

        if n1 == n2:
            return (path, totalValue)
        elif not len(self.g[n1]):
            return None

        for n in self.g[n1]:
            if not visited[n[0]]:
                p  = path.copy()
                p.append(n[0])
                sh = self.shortestPathHelper(n[0], n2, visited, totalValue + n[1], p)

                if sh != None:
                    r.append(sh)

        if not r:
            return None
        else:
            m = r[0]
            for i in r:
                if i[1] < m[1]:
                    m = i
                    
            return m
                    
        
    def shortestPath(self, n1, n2):
        res = self.shortestPathHelper(n1, n2, [False]* self.n, 0, [n1])

        return res if res != None else "sorry"

def main():
    while True:
        n = int(input(""))
        g = Graph(n)
    
        for _ in range(int(input(""))):
            v = list(map(int, input("").split(" ")))
            g.addEdge(v[0], v[1], v[2])
    
        camino = ""
    
        n1,n2 = list(map(int, input("").split(" ")))
        res = g.shortestPath(n1,n2)
    
        if res == "sorry":
            print(res)
        else:
            for c in res[0]:
                camino = camino + str(c) + (" -> " if c is not n2 else "")
            print("Path: " + camino, "Distance: " + str(res[1]))

main()
"""
g = Graph(5)
g.addEdge(0,1,20)
g.addEdge(0,2,35)
g.addEdge(4,2,35)
g.addEdge(4,1,250)
g.addEdge(4,3,1)
g.addEdge(0,3,20)

print(g.shortestPath(0,4))

g2 = Graph(5)
g2.addEdge(0,1,10)
g2.addEdge(0,4,350)
g2.addEdge(0,3,90)
g2.addEdge(1,3,25)
g2.addEdge(3,4,35)
g2.addEdge(2,3,190)

print(g2.shortestPath(0,4))
"""
