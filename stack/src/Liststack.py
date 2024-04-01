#ListQueue 구현해보자
import sys

# ListQueue.py 파일이 위치한 디렉토리의 절대 경로를 추가합니다.
# 예시 경로는 실제 경로로 대체해야 합니다.
sys.path.append('c:/Users/USER/structure-3/stack/src')



class liststack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
        
    def isEmpty(self) -> bool :
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()
        
    def prinStack(self):
        print("stack from top", end = ' ')
        for i in range(len(self.__stack)-1,-1,-1):
            print(self.__stack[i], end = ' ')
        print()