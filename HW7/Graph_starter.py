# This is starter code to help you represent a graph, if you want it
# This would help if you were using a reduction from some graph problem,
# such as vertex cover, independent set, (undirected) HP or HC, etc.






# Represents an undirected edge (u,v)
class Edge(object):
    def __init__(self, u, v):
        self.endpoints = set([u,v])

    def getEndpoints(self) :
	return self.endpoints

    def __repr__(self):
	return "%s" % (list(self.endpoints))


# Represents an undirected graph using an adjacency list graph representation
class Graph(object):
    def __init__(self):
	self.adj = {}
	self.edges = set()

    # Adds vertex v with no adjacencies initialy
    def addVertex(self, v):
	self.adj[v] = set() 

    # Returns the edges incident to vertex v
    def getEdges(self, v):
	return self.adj[v]

    # Returns all the edges in the graph as a set
    def getEdges(self):
	return self.edges

    # Returns the set of nodes adjacent to vertex v
    def getAdj(self, v):
	nbrs = set() 
	for e in self.adj[v] :
	    nbrs = nbrs.union( e.getEndpoints() )
	nbrs.remove( v )
	return nbrs 

    # Returns the set of all vertices
    def getVertices(self):
	return self.adj.keys()

    # Adds edge {u,v} to the graph by adding it to both
    # u and v's adjacency lists, as well as the edge set 
    def addEdge(self, u, v):
	if u == v:
	    raise ValueError( "u==v" )
	edge = Edge(u,v)
	self.adj[u].add( edge )
	self.adj[v].add( edge )
	self.edges.add( edge )
    
    def __repr__(self):
	s = ""
	for v in self.adj:
	    s += "%s: %s\n" % (v, list(self.adj[v]).__repr__())
	return s
	
					
# For example, here is a graph constructed using the class above
def graph1() :
    g = Graph()
    map( g.addVertex, ['s', 'a', 'b', 'c', 'd', 't'])
    g.addEdge( 's', 'a' )
    g.addEdge( 's', 'b' )
    g.addEdge( 's', 'd' )
    g.addEdge( 'a', 'b' )
    g.addEdge( 'a', 'c' )
    g.addEdge( 'b', 't' )
    g.addEdge( 'c', 't' )
    g.addEdge( 'd', 'a' )
    g.addEdge( 'd', 'c' )
    return g

# Here is a second example
def graph2() :
    g = Graph()
    map( g.addVertex, ['a', 'b', 'c', 'd', 'e', 'f'])
    g.addEdge( 'a', 'b' )
    g.addEdge( 'b', 'c' )
    g.addEdge( 'c', 'd' )
    g.addEdge( 'd', 'e' )
    g.addEdge( 'e', 'f' )
    return g


if __name__ == "__main__":    
    g = graph2()
    print g

