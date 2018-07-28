#!/usr/bin/env python3

# h3p2.py
# This program counts the number of significant inversions in
# a list of numbers
#
# This is just starter code, you fill in sortAndCount and 
# mergeAndCount!

import sys
import math
import readline

def sortAndCount(L):
    if(len(L) == 1):
        return 0, L
    else:
        A = L[0:int(len(L)/2)]
        B = L[int(len(L)/2):len(L)]
        (rA, A) = sortAndCount(A)
        (rB, B) = sortAndCount(B)
        (r, L) = mergeAndCount(A,B)
        return (r+rA+rB), L
    

def mergeAndCount(A, B):
    M = list()
    i = 0
    j = 0
    count = 0
    while((i < len(A)) & (j < len(B))):
    
        if(A[i] < B[j]):
            M.append(A[i])
            i = i + 1
        elif(A[i] > B[j]):
            M.append(B[j])
            j = j + 1
            count += len(A)-i
    if(i < len(A)):
        M.extend(A[i:])
    if(j < len(B)):
        M.extend(B[j:])
        
    return count, M



def main():
    
    #L = [2,4,1,3,5,7,6,8]
    #
    #(r, newList) = sortAndCount(L)
    #
    #print(r, " ", newList)

    s = sys.argv[1:]
    # If the user didn't pass in the list as arguments then
    # get the list of integers from the user
    
    if len(s)== 0:
        s = raw_input("Enter integers separated by spaces: ")
        s = s.split()

    # Convert the input into an array of integers
    # Catch errors related to non-integer arguments
    try:
        s = [int(x) for x in s]
    except:
        print( "Problem with the input, try again next time!" )
        return 1
    
    # Make sure the list is a power of two
    l = int( math.log( len(s), 2 ) )
    l = 2 ** l
    if( l != len(s) ) :
        print( "The list length was not a power of two, try again next time!")
        return 1
    
    r, L = sortAndCount(s)
    print("There are ", r, " significant inversions")

if __name__ == "__main__":
    main()

