import time

################ AVL Tree code ################

# AVL 트리의 노드 클래스 정의
class AVLNode:
    def __init__(self, newItem, left=None, right=None, h=1):
        self.item = newItem  # 노드에 저장된 값 (메모리 블록 크기)
        self.left = left  # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드
        self.height = h  # 노드의 높이
        self.start_address = None  # 메모리 블록의 시작 주소를 저장하기 위한 속성

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
            print("불가능한 타입! LL, LR, RR, RL 중 하나여야 합니다.")
        return returnNode

    # 좌회전
    def __leftRotate(self, t: AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "의 RChild는 NIL이 아니어야 합니다!")
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
            print(t.item, "의 LChild는 NIL이 아니어야 합니다!")
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

################ Hash Table code ################

# 해시 테이블 노드 클래스 정의, 연결리스트임
class HashTableNode:
    def __init__(self, key, start_address, size):
        self.key = key  # 노드의 키 값 (메모리 블록 ID)
        self.start_address = start_address  # 메모리 블록의 시작 주소
        self.size = size  # 메모리 블록의 크기
        self.next = None  # 다음 노드를 가리키는 포인터

# 해시 테이블 클래스 정의
class HashTable:
    def __init__(self, size):
        self.size = size  # 해시 테이블 크기
        self.table = [None] * size  # 해시 테이블 초기화

    # 해시 함수 정의
    def _hash(self, key):
        return key % self.size  # 나누기 방법 사용

    # 노드 삽입 , 체이닝 방법 사용
    def insert(self, key, start_address, size):
        index = self._hash(key)  # 해시 값을 기반으로 인덱스 계산
        new_node = HashTableNode(key, start_address, size)  # 새 노드 생성
        if self.table[index] is None:  # 인덱스 위치가 비어 있는 경우
            self.table[index] = new_node  # 새 노드를 해당 위치에 삽입
        else:  # 인덱스 위치가 비어 있지 않은 경우
            current = self.table[index]
            while current.next:  # 링크드 리스트의 끝을 찾아서
                current = current.next
            current.next = new_node  # 새 노드를 링크드 리스트의 끝에 삽입

    # 노드 제거
    def remove(self, key):
        index = self._hash(key)  # 해시 값을 기반으로 인덱스 계산
        current = self.table[index]
        prev = None
        while current:  # 링크드 리스트를 순회하며 노드 찾기
            if current.key == key:  # 노드를 찾은 경우
                if prev:  # 이전 노드가 있는 경우
                    prev.next = current.next  # 이전 노드의 다음 포인터를 현재 노드의 다음 노드로 설정
                else:  # 이전 노드가 없는 경우 (첫 번째 노드인 경우)
                    self.table[index] = current.next  # 인덱스 위치를 현재 노드의 다음 노드로 설정
                return current  # 제거된 노드를 반환
            prev = current
            current = current.next
        return None  # 노드를 찾지 못한 경우

    # 노드 찾기
    def find(self, key):
        index = self._hash(key)  # 해시 값을 기반으로 인덱스 계산
        current = self.table[index]
        while current:  # 링크드 리스트를 순회하며 노드 찾기
            if current.key == key:  # 노드를 찾은 경우
                return current  # 노드를 반환
            current = current.next
        return None  # 노드를 찾지 못한 경우

################ Allocator class ################

# 메모리 할당자 클래스 정의
class Allocator:
    def __init__(self):
        self.chunk_size = 4096  # 청크 크기 (메모리 블록의 단위 크기)
        self.free_list = AVLTree()  # 자유 영역을 관리하는 AVL 트리
        self.allocated_list = HashTable(1024)  # 할당된 영역을 관리하는 해시 테이블
        self.arena_size = 0  # 전체 할당된 메모리 크기

    # 메모리 할당 통계 출력
    def print_stats(self):
        total_memory = self.arena_size
        used_memory = sum(node.size for node in self._iter_hash_table())  # 사용 중인 메모리 크기 계산
        utilization = used_memory / total_memory if total_memory > 0 else 0  # 메모리 사용률 계산
        print(f"Arena: {total_memory / (1024 * 1024):.4f} MB")  # 전체 메모리 크기 출력
        print(f"In-use: {used_memory / (1024 * 1024):.4f} MB")  # 사용 중인 메모리 크기 출력
        print(f"Utilization: {utilization:.4f}")  # 메모리 사용률 출력

    # 메모리 할당
    def malloc(self, id, size):
        node = self.free_list.find(size)  # 요청된 크기 이상의 블록 찾기
        if node:  # 적절한 블록을 찾은 경우
            self.free_list.delete(node.item)  # 찾은 블록 삭제
            start_address = node.start_address
            remaining_size = node.item - size
            if remaining_size > 0:  # 남은 크기가 있는 경우
                self.free_list.insert(remaining_size, start_address + size)  # 남은 크기를 자유 리스트에 삽입
        else:  # 적절한 크기의 블록을 찾지 못한 경우
            start_address = self.arena_size
            self.arena_size += self.chunk_size
            remaining_size = self.chunk_size - size
            if remaining_size > 0:  # 남은 크기가 있는 경우
                self.free_list.insert(remaining_size, start_address + size)  # 남은 크기를 자유 리스트에 삽입
        self.allocated_list.insert(id, start_address, size)  # 할당된 블록을 할당 리스트에 추가
        return start_address

    # 메모리 해제
    def free(self, id):
        node = self.allocated_list.remove(id)  # 할당된 블록 찾기
        if node:  # 블록을 찾은 경우
            self.free_list.insert(node.size, node.start_address)  # 해제된 블록을 자유 리스트에 삽입

    # 해시 테이블을 순회하는 도우미 함수
    def _iter_hash_table(self):
        for i in range(self.allocated_list.size):
            current = self.allocated_list.table[i]
            while current:
                yield current  # 현재 노드를 반환
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

#                if n % 100 == 0:
#                   print(n, "...")
                
#                n += 1

    allocator.print_stats()  # 메모리 할당 통계 출력

# 코드 실행 시간 측정 종료
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.4f} seconds")
