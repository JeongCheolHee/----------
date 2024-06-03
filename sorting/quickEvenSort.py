import sys
sys.path.append('c:/Users/USER/structure-3/sorting')


def quickEvenSort(A, p:int, r:int):
    if p < r:
        q, t = partitionEven(A, p, r)
        quickEvenSort(A, p, q - 1)
        quickEvenSort(A, t + 1, r)

def partitionEven(A, p, r):
    x = A[r]  # 피벗 선택 (맨 끝 원소)
    i = p - 1  # x보다 작은 원소들의 끝 지점
    t = r  # x와 같은 원소들의 시작 지점 (처음에는 맨 끝 원소에서 시작)
    j = p
    while j < t:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            j += 1
        elif A[j] > x:
            t -= 1
            A[j], A[t] = A[t], A[j]
        else:
            j += 1
    A[t], A[r] = A[r], A[t]  # 피벗을 중간으로 이동
    return i + 1, t