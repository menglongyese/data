from pprint import  pformat
from typing import List
class Node :
     def __init__(self ,data):
         self.data=data
         self.parent=None
         self.left=None
         self.right=None
     def __repr__(self):
         if self.left is None and self.right is None:
             return str(self.data)
         return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)

class BST:
    def __init__(self):
        self.root=None

    def is_empty(self):
        if self.root  is None:
            return True
        else:
            return False
    def __insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
        else:
            parent_node=self.root
            while True:
                if new_node.data<parent_node.data:
                    if parent_node.left is None:
                        parent_node.left=new_node
                        break
                    else:
                        parent_node=parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right=new_node
                        break
                    else:
                        parent_node=parent_node.right
            new_node.parent = parent_node

    def insert(self, *args: List):
        for i in args:
            self.__insert(i)
        return self.root

if __name__ == '__main__':
    bst = BST().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    print(bst)





















