import sys
sys.path.append('c:/Users/USER/structure-3/sorting')

def shellSort(A):
    H = gapSequence(len(A))
    for h in H:
        for k in range(h):
            stepInsertionSort(A,k,h)
            
def stepInsertionSort(A, k:int, h:int):
    for i in range(k+h, len(A),h):
        j = i - h
        newItem = A[i]
        while 0 <= j and newItem < A[j]:
            A[j+h] = A[j]
            j -= h
        A[j + h] = newItem



def gapSequence(n : int) -> list: # h 수열(gap수열) 만들기
    H = [1]; gap = 1 # H(gap수열 리스트)
    while gap < n/5:
        gap = 3 * gap + 1
        H.append(gap)
    H.reverse()
    return H