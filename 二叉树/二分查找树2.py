from pprint import  pformat
from typing import List

class Node :
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None
    def __repr__(self):
        if self.left is None and self.right:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)
class BST:
    def __init__(self):
        self.root=None
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        if self.root is None :
            return True
        else:
            return False
    def __insert(self,data):
        new_node=Node(data,None)
        if self.is_empty():
            self.root=new_node
        else:
            cur_node=self.root
            while True:
                if new_node.data<cur_node.data:
                    if cur_node.left is None:
                        cur_node.left=new_node
                        break
                    else:
                        cur_node=cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.right=new_node
                        break
                    else:
                        cur_node=cur_node.right
            new_node.parent=cur_node
    def insert(self,*list):
        for i in list:
            self.__insert(i)
        return self
    def search(self,data):
        if self.root is Node:
            raise Exception('空二叉树')
        else:
            node=self.root
            while node and node.data !=data:
                node = node.left if data<node.data else node.right
            print(node)
            return node
    def is_right(self,node):
        return  node==node.parent.right
    def __reassign_node(self,node,new_children):
        if new_children is not None:
            new_children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=new_children
            else:
                node.parent.left=new_children
        else:
            self.root=new_children
    def get_max(self,node):
        if node is None :
            node=self.root
        else:
            while node.right is not None:
                node=node.right
        return node
    def remove(self,data):
        node=self.search(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_node(node,None)
            elif node.left is None:
                self.__reassign_node(node,node.right)
            elif node.right is None:
                self.__reassign_node(node,node.left)
            else:
                tmp=self.get_max(node.left)
                self.remove(tmp.data)
                node.data=tmp.data

if __name__ == '__main__':
    bst=BST().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    print(bst)
    bst.remove(6)
    print(bst)
