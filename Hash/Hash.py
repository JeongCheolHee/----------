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
