import sys
sys.path.append('c:/Users/USER/structure-3/sorting')


def Quicksort(A, p:int, r:int):
     if p<r:
         q = partition(A,p,r)
         Quicksort(A, p, q-1)
         Quicksort(A, q+1, r)


def partition(A, p:int, r:int)->int:
    x = A[r] # 맨 끝 원;소를 기준 원소로 삼기
    i = p-1 # i : 1구역의 끝 지점 (x보다 작은 애들 중 가장 오른쪽)
    for j in range(p,r): # 비교 인덱스 j
        if A[j] < x :
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i+1]
    return i + 1   