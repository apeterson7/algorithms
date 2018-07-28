# FF_starter.py
# This program implements the Ford Fulkerson algorithm
# to compute the maximum flow in an s-t- flow network
#
# This is just starter code, you fill in both
# findPath()
# maxFlow()
# If you have questions about how the given code works
# Please post your questions on piazza and someone will help!




# Represents a directed edge (u,v) of capacity c
# isFwd is a boolean representing whether (u,v) is a forwards edge
class Edge(object):
    def __init__(self, u, v, c, isFwd):
        self.start = u 
        self.end = v
        self.capacity = c
        self.isFwd = isFwd

    def __repr__(self):
        return "%s->%s:%s f?%s" % (self.start, self.end, self.capacity, self.isFwd)
    
# Represents an s-t flow network using an adjacency list graph representation
# (Each vertex keeps a list of all edges incident to it (both in and out))
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
        self.visited = {}
    
    # add vertex to the list of vertices, give it an empty adjacency list 
    def addVertex(self, vertex):
        self.adj[vertex] = []
        
    # return the set of incident edges to given vertex
    def getEdges(self, vertex):
        return self.adj[vertex]
    
    def getFlow(self, edge):
        return self.flow[edge]
    
    # add the edge (u,v) of capacity c to the network
    # also add the edge (v,u) of capacity 0 to the network
    # initialize both edges' flows to 0, and have them point to each other
    def addEdge(self, u, v, c=0):
        # cannot add self-loops
        if u == v:
            raise ValueError( "u==v" )
        
        # create the forward edge u->v and add it to u's adjacency list
        edge_forwards = Edge(u,v,c,True)
        self.adj[u].append( edge_forwards )
        self.flow[edge_forwards] = 0
        
        # create the backwards edge v->u and add it to v's adjacency list
        edge_backwards = Edge(v,u,0,False)
        self.adj[v].append( edge_backwards )
        self.flow[edge_backwards] = 0
        
        # allow the forwards and backwards edges pointers to each other
        edge_forwards.reverse = edge_backwards
        edge_backwards.reverse = edge_forwards
        
        
    def __repr__(self):
        s = ""
        for v in self.adj:
            s += "%s: %s\n" % (v, self.adj[v].__repr__())
        return s
    
    def printFlow(self):
        for key in self.flow:
            if self.flow[key] > 0 :
                print "%s: %s" % (key, self.flow[key])

    
    # TODO: Complete this method
    # returns a simple path in the residual graph from start to end, if it exists
    # I recommend implementing this function as a recursive dfs
    def findPath(self, start, end, P):
        if(start == end):
            self.visited = {}
            return P
        self.visited[start] = 0
        print(self.visited)
        adjEdges = self.getEdges(start)
        for edge in adjEdges:
            print(edge, edge.end in self.visited)
            if edge.capacity > 0 & (edge.end in self.visited) == False:
                    P.append(edge)
                    print(P)
                    return self.findPath(edge.end, end, P)
                    # print(newP)
                    # if newP[len(newP)-1] == end:
                    #     return newP
        return 0

    # TODO: Complete this method 
    # returns the value of the maximum source-sink flow using Ford-Fulkerson
    # it also computes the flow itself 
    def maxFlow(self, source, sink):
        P = self.findPath(source,sink,[])
        #while(P != -1):
        for i in range(1):
            #determine the bottleneck
            b = 100
            for e in P:
                if e.capacity < b:
                    b = e.capacity
            #add to the flow
            for e in P:
                if e.isFwd == True:
                    self.flow[e] = self.getFlow(e) + b
                else:
                    self.flow[e] = self.getFlow(e) - b
            #create residual graph
            for e in P:
                e.capacity = e.capacity - b
                e.reverse.capacity = e.reverse.capacity + b
            #find a path from s to t
            print g

            P = self.findPath(source,sink,[])

        #add up flow leaving s
        maxFlow = 0
        for e in self.getEdges(source):
            maxFlow += self.getFlow(e)
        return maxFlow

def worksheetGraph():
    g = FlowNetwork()
    map( g.addVertex, ['s', 'a', 'b', 'c', 'd', 't'])
    g.addEdge( 's', 'a', 3)
    g.addEdge( 's', 'b', 1)
    g.addEdge( 's', 'd', 8)
    g.addEdge( 'a', 'b', 8)
    g.addEdge( 'a', 'c', 2)
    g.addEdge( 'b', 't', 10)
    g.addEdge( 'c', 't', 3)
    g.addEdge( 'd', 'a', 4)
    g.addEdge( 'd', 'c', 1)
    return g


if __name__ == "__main__":    
    g = worksheetGraph()
    print "Input graph:"
    print g
    print "*"* 40
    #print(g.findPath('s','t',[]))
    v = g.maxFlow('s', 't')
    print "Value of Max Flow: ", v
    #g.printFlow()
    #print g
