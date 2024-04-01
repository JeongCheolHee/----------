# 2. 비효율적이지만 2개의 큐를 사용하여 스택의 push() 와 pop() 알고리즘을 작성하시오

from src.ListQueue import *

class QueStack():
    def __init__(self):
        self.__Qu1 = ListQueue()
        self.__Qu2 = ListQueue()
        
    def push(self,x):
        self.__Qu1.enqueue(x)

    def pop(self):
        if self.__Qu1.isEmpty():
            return None
        while self.__Qu1.size() > 1: # 마지막 요소를 제외한 모든 요소 이동
            self.__Qu2.enqueue(self.__Qu1.dequeue())
        last_item = self.__Qu1.dequeue()
        self.__Qu1, self.__Qu2 = self.__Qu2, self.__Qu1 # 큐 교체
        return last_item
    

        
que_stack = QueStack()
que_stack.push('abc')
que_stack.push('123')
que_stack.push('421412421')
print(que_stack.pop())
        
        




