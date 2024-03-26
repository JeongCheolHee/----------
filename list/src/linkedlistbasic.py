# LinkedListBasic 구현

from .listnode import ListNode

class LinkedListBasic:
    def __init__(self):
       self.__head = ListNode("dummy", None)
       self.__numItems = 0
    
    def __getNode(self, i:int) -> ListNode:
        if i >= self.__numItems:
            return None
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr

        
    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)            # prev 이전 노드
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": list범위 넘어서부렸어")
            
    def append(self, newItem):
        prev = self.__getNode(self.__numItems -1) # 마지막에 추가함
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1
        
    def pop(self, i: int):
        # 음수 인덱스를 양수 인덱스로 변환
        if i < 0:
            i += self.__numItems

        if 0 <= i < self.__numItems:
            prev = self.__getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            self.__numItems -= 1
            return curr.item
        else:
            print(f"Index {i} is out of bounds")
            return None

        
    def __findNode(self,x):
        prev = self.__head # 더미헤드
        curr = prev.next # 0번 노드
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)
    
    def remove(self, x) : # 연결리스트 원소 x 삭제하기
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -=1
            return x
        else:
            return None
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def get(self, i:int): # i번째 원소 알려주기
        if self.isEmpty():  # isEmpty 메서드 호출 수정
            print("List is empty")
            return None
        if (i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            print(f"Index {i} is out of bounds")
            return None

        
    def index(self, x) -> int: # 원소의 인덱스 알아내기
        curr = self.__head.next # 0번 노드 : 더미 헤드 다음 노드
        for index in range(self.__numItems):
            if curr.item == x:
                print("해당 원소는 :", index, "번 째 원소")
            else:
                curr = curr.next
        return print("사용하지 않는 인덱스")
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0
    
    def count(self, x) -> int: # 해당 원소 개수 세기
        cnt = 0
        curr = self.__head.next # 더미 노드 다음 노드
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        
        return cnt
    
    def extend(self, a): # a는 self와 같은 타입의 리스트
        for index in range(a.size()):
            self.append(a.get(index))
            
    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self):         
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))    #
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
            
    def sort(self):
        a = []
        for index in range(self.__numItems):
            item = self.get(index)
            if item is not None:  # None 값 제외
                a.append(item)
        a.sort()
        self.clear()
        for item in a:
            self.append(item)
            
    def printList(self):
        curr = self.__head.next  # 더미 헤드의 다음 노드부터 시작
        items = []  # 모든 아이템을 담을 리스트
        while curr is not None:
            items.append(curr.item)  # 현재 노드의 아이템을 리스트에 추가
            curr = curr.next  # 다음 노드로 이동
        print(' '.join(map(str, items)))  # 모든 아이템을 문자열로 변환하여 공백으로 구분


        
    def __iter__(self):
        return LinkedListBasicIterator(self)

class LinkedListBasicIterator:
    def __init__(self, alist):
        self.curr = alist._LinkedListBasic__head.next
        
    def __next__(self):
        if self.curr is None:
            raise StopIteration
        else:
            item = self.curr.item
            self.curr = self.curr.next
            return item  