import time

################ Red Black Tree code ################

class RedBlackNode:
    def __init__(self, item, left=None, right=None, parent=None, color='red'):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
        self.start_address = None  # 추가: start_address 속성 추가

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(None, color='black')
        self.root = self.NIL

    def find(self, size):
        return self.__findMinLargerEqual(self.root, size)

    def __findMinLargerEqual(self, node, size):
        if node == self.NIL:
            return None
        elif node.item >= size:
            left_res = self.__findMinLargerEqual(node.left, size)
            if left_res:
                return left_res
            return node
        else:
            return self.__findMinLargerEqual(node.right, size)

    def insert(self, size, start_address):
        new_node = RedBlackNode(size, left=self.NIL, right=self.NIL, parent=None)
        new_node.start_address = start_address
        if self.root == self.NIL:
            self.root = new_node
            self.root.color = 'black'
        else:
            self.__insertNode(self.root, new_node)
            self.__fixInsert(new_node)

    def __insertNode(self, root, node):
        if node.item < root.item:
            if root.left == self.NIL:
                root.left = node
                node.parent = root
            else:
                self.__insertNode(root.left, node)
        else:
            if root.right == self.NIL:
                root.right = node
                node.parent = root
            else:
                self.__insertNode(root.right, node)

    def __fixInsert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__leftRotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__rightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__rightRotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.__leftRotate(node.parent.parent)
        self.root.color = 'black'

    def __leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, item):
        node = self.__searchItem(self.root, item)
        if node == self.NIL:
            return
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.__transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.__transplant(node, node.left)
        else:
            y = self.__minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'black':
            self.__fixDelete(x)

    def __searchItem(self, tNode, x):
        if tNode == self.NIL:
            return self.NIL
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)

    def __transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def __fixDelete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.__leftRotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.__rightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.__leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.__rightRotate(x.parent)
                    w = x.parent.left
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.__leftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.__rightRotate(x.parent)
                    x = self.root
        x.color = 'black'


################ Hash Table code ################

class HashTableNode:
    def __init__(self, key, start_address, size):
        self.key = key
        self.start_address = start_address
        self.size = size
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key, start_address, size):
        index = self._hash(key)
        new_node = HashTableNode(key, start_address, size)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return current
            prev = current
            current = current.next
        return None

    def find(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

################ Allocator class ################

class Allocator:
    def __init__(self):
        self.chunk_size = 4096
        self.free_list = RedBlackTree()
        self.allocated_list = HashTable(1024)  # 해시 테이블 크기는 임의로 1024로 설정
        self.arena_size = 0

    def print_stats(self):
        total_memory = self.arena_size
        used_memory = sum(node.size for node in self._iter_hash_table())
        utilization = used_memory / total_memory if total_memory > 0 else 0
        print(f"Arena: {total_memory / (1024 * 1024):.2f} MB")
        print(f"In-use: {used_memory / (1024 * 1024):.2f} MB")
        print(f"Utilization: {utilization:.2f}")

    def malloc(self, id, size):
        node = self.free_list.find(size)
        if node:
            self.free_list.delete(node.item)
            start_address = node.start_address
            remaining_size = node.item - size
            if remaining_size > 0:
                self.free_list.insert(remaining_size, start_address + size)
        else:
            start_address = self.arena_size
            self.arena_size += self.chunk_size
            remaining_size = self.chunk_size - size
            if remaining_size > 0:
                self.free_list.insert(remaining_size, start_address + size)
        self.allocated_list.insert(id, start_address, size)
        return start_address

    def free(self, id):
        node = self.allocated_list.remove(id)
        if node:
            self.free_list.insert(node.size, node.start_address)

    def _iter_hash_table(self):
        for i in range(self.allocated_list.size):
            current = self.allocated_list.table[i]
            while current:
                yield current
                current = current.next

################ Main execution ################

start_time = time.time()

if __name__ == "__main__":
    
    allocator = Allocator()

    with open("C:\\Users\\USER\\structure-3\\Homework\\allocator\\input.txt", "r") as file:
        n = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                allocator.free(int(req[1]))

#                if n % 100 == 0:
#                   print(n, "...")
                
#                n += 1

    allocator.print_stats()
 
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.4f} seconds")
