# Heap 구현
import sys
sys.path.append('c:\\Users\\USER\\structure-3\\Heap\\src')

class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []
            
    
    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)
    
    # 스며 오르기 
    def __percolateUp(self, i:int):
        parent = ( i - 1 ) // 2
        if i > 0 and self.__A[i] < self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
            
            
    def deleteMin(self):
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None
        
    # 스며내리기
    
    def __percolateDown(self, i : int):
        child = 2 * i  + 1
        right = 2 * i  + 2 
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A) - 1 and self.__A[child] > self.__A[right]):
                child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
                
    def max(self):
        return self.__A[0]
    
    
    # 힙 만들기 
    def buildHeap(self):
        for i in range((len(self.__A) - 2) // 2,-1,-1):
            self.__percolateDown(i)
        
    # 힙이 비었는지 확인하기
    
    def isEmpty(self) -> bool:
        return len(self.__A) == 0
    
    def clear(self):
        self.__A = []
        
    def size(self) -> int: 
        return len(self.__A)
    
    
    def heapPrint(self):
        # 노드를 하나씩 출력.
        for i in range(len(self.__A)):
            # 새로운 레벨이 시작될 때마다 줄바꿈을 추가
            if i == 0 or i & (i + 1) == 0:
                print()
            print(self.__A[i], end=' ')
        print("\n" + "=" * 25)
    
        


        
        

    
    
                        




 











