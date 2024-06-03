import time

# AVL 트리의 노드 클래스 정의
class AVLNode:
    def __init__(self, newItem, left, right, h):
        self.item = newItem  # 노드에 저장된 값 (메모리 블록 크기)
        self.left = left  # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드
        self.height = h  # 노드의 높이
        self.start_address = None  # 메모리 블록의 시작 주소

# AVL 트리 클래스 정의
class AVLTree:
    def __init__(self):
        self.NIL = AVLNode(None, None, None, 0)  # NIL 노드 초기화 (빈 노드를 나타냄)
        self.__root = self.NIL  # 루트 노드 초기화
        self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4  # 회전 타입 상수 정의
        self.NO_NEED = 0  # 균형 맞추기 필요 없음
        self.ILLEGAL = -1  # 불가능한 회전 타입

    # 특정 항목을 검색
    def search(self, x):
        return self.__searchItem(self.__root, x)

    # 재귀적으로 항목 검색
    def __searchItem(self, tNode, x):
        if tNode == self.NIL:
            return self.NIL  # 항목을 찾지 못함
        elif x == tNode.item:
            return tNode  # 항목을 찾음
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)  # 왼쪽 서브트리에서 검색
        else:
            return self.__searchItem(tNode.right, x)  # 오른쪽 서브트리에서 검색

    # 주어진 크기 이상인 최소 노드 찾기
    def find(self, size):
        return self.__findMinLargerEqual(self.__root, size)

    # 재귀적으로 주어진 크기 이상의 최소 노드 찾기
    def __findMinLargerEqual(self, tNode, size):
        if tNode == self.NIL:
            return None  # 노드를 찾지 못함
        elif tNode.item >= size:
            left_res = self.__findMinLargerEqual(tNode.left, size)
            if left_res:
                return left_res  # 왼쪽 서브트리에서 적합한 노드가 있으면 반환
            return tNode  # 현재 노드가 적합한 경우
        else:
            return self.__findMinLargerEqual(tNode.right, size)

    # 노드 삽입
    def insert(self, size, start_address):
        self.__root = self.__insertItem(self.__root, size, start_address)

    # 재귀적으로 노드 삽입
    def __insertItem(self, tNode: AVLNode, size, start_address) -> AVLNode:
        if tNode == self.NIL:  # 빈 트리에 삽입
            tNode = AVLNode(size, self.NIL, self.NIL, 1)
            tNode.start_address = start_address  # 시작 주소 설정
        elif size < tNode.item:  # 왼쪽 서브트리에 삽입
            tNode.left = self.__insertItem(tNode.left, size, start_address)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
            type = self.__needBalance(tNode)  # 균형 필요 여부 확인
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
        else:  # 오른쪽 서브트리에 삽입
            tNode.right = self.__insertItem(tNode.right, size, start_address)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
            type = self.__needBalance(tNode)  # 균형 필요 여부 확인
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
        return tNode

    # 노드 삭제
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    # 재귀적으로 노드 삭제
    def __deleteItem(self, tNode: AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            return self.NIL  # 항목을 찾지 못함
        else:
            if x == tNode.item:  # 항목을 찾음
                tNode = self.__deleteNode(tNode)  # 노드 삭제
            elif x < tNode.item:  # 왼쪽 서브트리에서 검색
                tNode.left = self.__deleteItem(tNode.left, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
                type = self.__needBalance(tNode)  # 균형 필요 여부 확인
                if type != self.NO_NEED:
                    tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
            else:  # 오른쪽 서브트리에서 검색
                tNode.right = self.__deleteItem(tNode.right, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
                type = self.__needBalance(tNode)  # 균형 필요 여부 확인
                if type != self.NO_NEED:
                    tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
            return tNode

    # 노드 삭제 후 균형 맞추기
    def __deleteNode(self, tNode: AVLNode) -> AVLNode:
        if tNode.left == self.NIL and tNode.right == self.NIL:  # 자식이 없는 경우
            return self.NIL
        elif tNode.left == self.NIL:  # 오른쪽 자식만 있는 경우
            return tNode.right
        elif tNode.right == self.NIL:  # 왼쪽 자식만 있는 경우
            return tNode.left
        else:  # 두 자식이 모두 있는 경우
            rtnItem, rtnNode = self.__deleteMinItem(tNode.right)  # 오른쪽 서브트리에서 최소 항목 찾기
            tNode.item = rtnItem.item  # 최소 항목으로 교체
            tNode.start_address = rtnItem.start_address  # 시작 주소 복사
            tNode.right = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
            type = self.__needBalance(tNode)  # 균형 필요 여부 확인
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
            return tNode

    # 최소 항목 삭제
    def __deleteMinItem(self, tNode: AVLNode) -> tuple:
        if tNode.left == self.NIL:
            return tNode, tNode.right
        else:
            rtnItem, rtnNode = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)  # 높이 갱신
            type = self.__needBalance(tNode)  # 균형 필요 여부 확인
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)  # 균형 맞추기
            return rtnItem, tNode
        
    # AVL 트리 균형 맞추기
    def __balanceAVL(self, tNode: AVLNode, type: int) -> AVLNode:
        returnNode = self.NIL
        if type == self.LL:
            returnNode = self.__rightRotate(tNode)  # LL 회전
        elif type == self.LR:
            tNode.left = self.__leftRotate(tNode.left)
            returnNode = self.__rightRotate(tNode)  # LR 회전
        elif type == self.RR:
            returnNode = self.__leftRotate(tNode)  # RR 회전
        elif type == self.RL:
            tNode.right = self.__rightRotate(tNode.right)
            returnNode = self.__leftRotate(tNode)  # RL 회전
        else:
            print("불가능한 타입 LL, LR, RR, RL 중 하나여야 함")
        return returnNode

    # 좌회전
    def __leftRotate(self, t: AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "의 RChild는 NIL이 아니어야 함")
        RLChild = RChild.left
        RChild.left = t
        t.right = RLChild
        t.height = 1 + max(t.left.height, t.right.height)  # 높이 갱신
        RChild.height = 1 + max(RChild.left.height, RChild.right.height)  # 높이 갱신
        return RChild

    # 우회전
    def __rightRotate(self, t: AVLNode) -> AVLNode:
        LChild = t.left
        if LChild == self.NIL:
            print(t.item, "의 LChild는 NIL이 아니어야 함")
        LRChild = LChild.right
        LChild.right = t
        t.left = LRChild
        t.height = 1 + max(t.left.height, t.right.height)  # 높이 갱신
        LChild.height = 1 + max(LChild.left.height, LChild.right.height)  # 높이 갱신
        return LChild

    # 트리 균형 필요 여부 판단
    def __needBalance(self, t: AVLNode) -> int:
        type = self.ILLEGAL
        if t.left.height + 2 <= t.right.height:  # 오른쪽 서브트리가 높음
            if t.right.left.height <= t.right.right.height:
                type = self.RR  # RR 회전 필요
            else:
                type = self.RL  # RL 회전 필요
        elif t.left.height >= t.right.height + 2:  # 왼쪽 서브트리가 높음
            if t.left.left.height >= t.left.right.height:
                type = self.LL  # LL 회전 필요
            else:
                type = self.LR  # LR 회전 필요
        else:
            type = self.NO_NEED  # 균형 필요 없음
        return type

    # 트리가 비었는지 확인
    def isEmpty(self) -> bool:
        return self.__root == self.NIL

    # 트리 초기화
    def clear(self):
        self.__root = self.NIL

# 이중 연결 리스트의 노드 클래스 정의
class DoublyLinkedListNode:
    def __init__(self, key, start_address, size):
        self.key = key  # 노드의 키 값 (메모리 블록 ID)
        self.start_address = start_address  # 메모리 블록의 시작 주소
        self.size = size  # 메모리 블록의 크기
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터

# 이중 연결 리스트 클래스 정의
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드
        self.tail = None  # 리스트의 마지막 노드

    # 노드를 리스트 끝에 추가
    def append(self, key, start_address, size):
        new_node = DoublyLinkedListNode(key, start_address, size)
        if not self.head:  # 리스트가 비어있는 경우
            self.head = self.tail = new_node
        else:  # 리스트가 비어있지 않은 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 노드를 리스트에서 제거
    def remove(self, node):
        if not node.prev:  # 첫 번째 노드인 경우
            self.head = node.next
        else:
            node.prev.next = node.next
        if not node.next:  # 마지막 노드인 경우
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    # 키 값으로 노드 찾기
    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

# 메모리 할당자 클래스 정의
class Allocator:
    def __init__(self):
        self.chunk_size = 4200  # 청크 크기 (메모리 블록의 단위 크기)
        self.free_list = AVLTree()  # 자유 영역을 관리하는 AVL 트리
        self.allocated_list = DoublyLinkedList()  # 할당된 영역을 관리하는 이중 연결 리스트
        self.arena_size = 0  # 전체 할당된 메모리 크기

    # 메모리 할당 통계 출력
    def print_stats(self):
        total_memory = self.arena_size
        used_memory = sum(node.size for node in self._iter_list(self.allocated_list.head))
        utilization = used_memory / total_memory if total_memory > 0 else 0
        print(f"Arena: {total_memory / (1024 * 1024):.4f} MB")
        print(f"In-use: {used_memory / (1024 * 1024):.4f} MB")
        print(f"Utilization: {utilization:.4f}")

    # 메모리 할당
    def malloc(self, id, size):
        node = self.free_list.find(size)  # 요청된 크기 이상의 블록 찾기
        if node:
            self.free_list.delete(node.item)  # 찾은 블록 삭제
            start_address = node.start_address
            remaining_size = node.item - size
            if remaining_size > 0:
                self.free_list.insert(remaining_size, start_address + size)  # 남은 크기를 자유 리스트에 삽입
        else:  # 적절한 크기의 블록을 찾지 못한 경우
            start_address = self.arena_size
            self.arena_size += self.chunk_size
            remaining_size = self.chunk_size - size
            if remaining_size > 0:
                self.free_list.insert(remaining_size, start_address + size)  # 남은 크기를 자유 리스트에 삽입
        self.allocated_list.append(id, start_address, size)  # 할당된 블록을 할당 리스트에 추가
        return start_address

    # 메모리 해제
    def free(self, id):
        node = self.allocated_list.find(id)  # 할당된 블록 찾기
        if node:
            self.free_list.insert(node.size, node.start_address)  # 해제된 블록을 자유 리스트에 삽입
            self.allocated_list.remove(node)  # 할당 리스트에서 노드 제거

    # 이중 연결 리스트를 반복하는 도우미 함수
    def _iter_list(self, head):
        current = head
        while current:
            yield current
            current = current.next

# 코드 실행 시간 측정 시작
start_time = time.time()

if __name__ == "__main__":
    
    allocator = Allocator()

    # 입력 파일 읽기
    with open("C:\\Users\\USER\\structure-3\\Homework\\allocator\\input.txt", "r") as file:
        n = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':  # 메모리 할당 요청
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':  # 메모리 해제 요청
                allocator.free(int(req[1]))

            # if n % 100 == 0:
            #     print(n, "...")
            
            # n += 1

    allocator.print_stats()  # 메모리 할당 통계 출력
 
# 코드 실행 시간 측정 종료
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.4f} seconds")
