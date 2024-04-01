#ListQueue 구현해보자
import sys

# ListQueue.py 파일이 위치한 디렉토리의 절대 경로를 추가합니다.
# 예시 경로는 실제 경로로 대체해야 합니다.
sys.path.append('c:/Users/USER/structure-3/Queue/src')


class ListQueue:
    def __init__(self):
        self.__queue = []
        
    def size(self):
        return len(self.__queue)
    
    def enqueue(self, x):
        self.__queue.append(x)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.__queue.pop(0)
        else:
            return None
        
    def front(self):
        if self.isEmpty():
            return None
        else:
            self.__queue[0]
            
    def isEmpty(self) -> bool:
        return len(self.__queue)==0 
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def printQueue(self):
        print("Queue from fornt" , end = ' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end = ' ')
        print()
        