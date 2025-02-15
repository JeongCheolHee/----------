class RBTreeNode:
    def __init__(self, key, start_address, size):
        self.key = key
        self.start_address = start_address
        self.size = size
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'R'  # New nodes are always red initially

class RedBlackTree:
    def __init__(self):
        self.NIL = RBTreeNode(None, None, None)
        self.NIL.color = 'B'
        self.root = self.NIL

    def find(self, size):
        node = self.root
        best_fit = None
        while node != self.NIL:
            if node.size >= size:
                best_fit = node
                node = node.left
            else:
                node = node.right
        return best_fit

    def insert(self, size, start_address):
        new_node = RBTreeNode(size, start_address, size)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.size < current.size:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.size < parent.size:
            parent.left = new_node
        else:
            parent.right = new_node

        self.__fix_insert(new_node)

    def __fix_insert(self, node):
        while node != self.root and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.__right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.__left_rotate(node.parent.parent)
        self.root.color = 'B'

    def __left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def __right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def delete(self, size):
        node = self.__find_node(self.root, size)
        if node is None or node == self.NIL:
            return
        original_color = node.color
        if node.left == self.NIL:
            x = node.right
            self.__transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.__transplant(node, node.left)
        else:
            y = self.__minimum(node.right)
            original_color = y.color
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
        if original_color == 'B':
            self.__fix_delete(x)

    def __find_node(self, node, size):
        while node != self.NIL:
            if node.size == size:
                return node
            elif node.size < size:
                node = node.right
            else:
                node = node.left
        return None

    def __minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def __transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __fix_delete(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.__left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.__right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.__left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.__right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'B' and w.left.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.__left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.__right_rotate(x.parent)
                    x = self.root
        x.color = 'B'
