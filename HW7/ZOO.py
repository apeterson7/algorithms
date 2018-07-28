# ZOO.py
# This program implements a brute-force solution to the ZOO problem
# It takes as input a set of m donor sets A1, A2, ... , Am and a natural number k
# It determines whether there is a set H of size k such that H contains
# at least one element from each of the Ai.
#
# You should not need to modify this code at all. You should only need
# to call ZOO as a "black box". Having said that, if you think the code
# is broken or if you have questions about it, please post your questions
# or concerns on piazza and someone will help!

import Graph_starter
import itertools

# Returns true if and only if Z has a ZOO set of size k
def determineZooSet( Z, k ):
    A = Z.getAnimals()

    # n = number of animals of Z 
    n = len(A)

    # for each subset H of k animals, check if it is a zoo
    for H in subsets(A,k) :
	if isZooSet( H, Z ) :
	    return True # we found one and that's all it takes!
    return False 


# Returns true if and only if H is a ZOO solution for Z
def isZooSet( H, Z ) :
    donors = Z.getDonors()

    # Check each donor's request and make sure we have at least one animal from each
    for d in donors :
	if len(Z.getDonor(d) & H) == 0 : # the intersection of H and this donor is 0
	    return False
    return True


# Returns all subsets of mySet of size k
def subsets(mySet, k) :
    return map(set, itertools.combinations(mySet, k))


# Represents a zoo instance
# I.e. a set of animals and a set of donor requests (subsets of animals)
# (We add the natural number k outside of this class for more flexibility)
class ZOO(object):
    def __init__(self):
	self.animals = set()
	self.donors = {}

    def addAnimal(self, a):
	self.animals.add( a )

    def addDonor(self,d) :
	self.donors[d] = set()

    def addDonor(self, d, requests) :
	self.animals = self.animals.union( requests ) 	
	self.donors[d] = requests

    def getAnimals(self) :
	return self.animals

    def getDonor(self, d):
	return self.donors[d]

    def getDonors(self):
	return self.donors

    def __repr__(self):
	s = ""
	s += "Animals: %s\n" % self.animals
	for d in self.donors:
	    s += "%s: %s\n" % (d, self.donors[d].__repr__())
	return s
	
					
# Use this example to help construct ZOO instances in your reduction
def donors1() :
    # Create an empty zoo instance
    z = ZOO()

    # Add animals explicitly. You can also just add them as donors request them.
    map( z.addAnimal, ["Cat", "Dog", "Pangolin", "Monkey", "Zebra"])

    # Add 3 donors. Note that donor 3 requests a lion which didn't exist in 
    # the current set of animals, so it is added
    z.addDonor( '1', set(["Cat"]) )
    z.addDonor( '2', set(["Pangolin", "Dog"]) )
    z.addDonor( '3', set(["Cat", "Dog", "Lion"]) )
    return z

def solveVCWithZoo(G, k):
    z = Z00()
    map( z.addAnimal, g.getVertices())

    count = 0
    for i in g.getEdges():
        z.addDonor(count, i.getEndpoints())
        count = count + 1
    return determineZooSet(z,k)


if __name__ == "__main__":    
    # z1 = donors1()
    # print z1
    # k = 2
    # print "For k=%s, ZOO is: " %k, determineZooSet(z1,k)
    # k = 1
    # print "For k=%s, ZOO is: " %k, determineZooSet(z1,k)

    g = Graph_starter.graph2()

    z = ZOO()
    map( z.addAnimal, g.getVertices())

    count = 0
    for i in g.getEdges():
        z.addDonor(count, i.getEndpoints())
        count = count + 1
    
    print z
    k = 4
    print "For k=%s, ZOO is: " %k, solveVCWithZoo(Graph_starter.graph2(),k)
    k = 2
    print "For k=%s, ZOO is: " %k, solveVCWithZoo(Graph_starter.graph2(),k)



        

