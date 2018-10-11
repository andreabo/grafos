class Graph(object):
    def __init__(self, n):
        self.g = {}
        self.n = n
        
        for i in range(n):
            self.g[i] = []
            
    def addEdge(self, n1, n2):
        if n1 not in self.g:
            self.g[n1] = []

        if n2 not in self.g:
            self.g[n2] = []
            
        self.g[n1].append(n2)
        self.g[n2].append(n1)
    

    def getPathHelper(self, n1, n2, visited, path):
        v = visited
        v[n1] = True

        r = None
        if n1 == n2:
            return path
        elif not len(self.g[n1]):
            return None
        elif not list(filter(lambda x: not visited[x], self.g[n1])):
            return None
        
        for n in self.g[n1]:
            if not v[n]:
                p = path.copy()
                print(p, n1, n, self.g[n1])
                p.append(n)
                sh = self.getPathHelper(n, n2, v, p)

                
                if sh != None:
                    return sh

        return r
        
    def findPath(self, n1, n2):
        visited = {}
        for city in self.g.keys():
            visited[city] = False

        res = self.getPathHelper(n1, n2, visited, [n1])

        return res if res != None else "sorry"

def main():
    while True:
        n = int(input(""))
        g = Graph(n)

        (m, t) = map(int, input("").split(" "))
        
        for _ in range(m):
            v = input("").split(" ")
            g.addEdge(v[0], v[1])

        testCases = []
        for y in range(t):
            print(y)
            testCases.append(input().split(" "))

        for t1 in testCases:
            camino = ""
            res = g.findPath(t1[0],t1[1])
            if res == "sorry":
                print(res)
            else:
                for c in res:
                    camino = camino + str(c)
                print("Path: " + camino)
    
main()
