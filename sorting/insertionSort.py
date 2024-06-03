import sys
sys.path.append('c:/Users/USER/structure-3/sorting')



def insertionSort(A):
    for i in range(1,len(A)):
        loc = i - 1
        newitem = A[i]
        while loc >= 0 and newitem < A[loc]:
            A[loc + 1] = A[loc]
            loc = 1 - loc
        A[loc+1] = newitem
        

            