# h4p2.py
# This program determines the maximum possible return with
# any k-shot strategy over n days, where day i has price p[i]
#
# This is just starter code, you fill in maxProfit(p)

import sys

def printArray(A):
    for row in A:
	print(row)


def maxProfit(p, k):
    M = [[0 for x in p] for x in range(k)]
    printArray(M)
    for j in range(1,len(p)):
	for b in range(1,k):
	    #Opt(j,b)
	    print(j,b)
	    highest = 0
	    best_i = 1
	    #find i such that p(j) - p(i) is maximized
	    for i in range(0,j-1):
		if((p[j] - p[i]) > highest):
		    best_i = i
	    temp = max((M[best_i-1][b-1] + p[j] - p[best_i]),M[j-1][b])
	    M[b][j] = temp
    
    
    printArray(M)
    return M[k-1][len(p)-1]


def main():
    s = sys.argv[1:]
    # If the user didn't pass in the list as arguments then
    # get the list of integers from the user
    if len(s)==0 :
        s = raw_input("Enter integers separated by spaces: ")
        s = s.split()
    # Convert the input into an array of integers
    # Catch errors related to non-integer arguments
    try:
        s = [int(x) for x in s]
    except:
        print( "Problem with the input, try again next time!" )
        return 1

    k = raw_input("Enter how many shots you have, i.e. k (-1 to stop): ")

    try:
        k = int(k)
    except:
        print( "Problem with the input, try an integer k next time!" )
        return 1

    while (k > 0) :
        profit = maxProfit(s, k)

        print ("There maximum return with any %d-shot strategy is %d" % (k, profit))
        k = raw_input("Enter how many shots, i.e. k (-1 to stop): ")
        try:
            k = int(k)
        except:
            print( "Problem with the input, try an integer k next time!" )
            return 1

if __name__ == "__main__":
    main()


