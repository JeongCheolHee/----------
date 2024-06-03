class TreeNode:
    def __init__(self, newitem, left, right):
        self.item = newitem
        self.left = left
        self.right = right
        

class BST:
    def __init__(self):
        self.__root = None
    
    # 검색 구현
    def search(self, x) -> TreeNode:
        return self.__searchItem(self.__root, x)            ######### self. 붙여야되는거 아닌가
    
    def __searchItem(self, tNode:TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None
        elif (x == tNode.item):
            return tNode
        elif (x < tNode.item):
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    # 삽입 구현
    def insert(self, newitem):
        self.__root = self.__insertItem(self.__root, newitem)
    
    def __insertItem(self, tNode:TreeNode, newitem)-> TreeNode:
        if (tNode == None):
            tNode = TreeNode(newitem, None, None)
        elif (newitem < tNode.item):
            tNode.left = self.__insertItem(tNode.left, newitem)
        else:
            tNode.right = self.__insertItem(tNode.right, newitem)
        return tNode
        
        
        
        
        