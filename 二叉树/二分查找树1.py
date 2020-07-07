from pprint import pformat
# from typing import List


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % ( self.data ): (self.left, self.right)}, indent=1)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, data):
        new_node = Node(data, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if new_node.data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif new_node.data >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *args):
        for i in args:
            self.__insert(i)
        return self

    def search(self, data):
        if self.root is None:
            raise Exception('空二叉树')
        else:
            node = self.root
            while node and node.data != data:
                node = node.left if data < node.data else node.right
            # print(node)
            return node

    def is_right(self, node):
        return node == node.parent.right

    def __reassign_node(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, data):
        node = self.search(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_node(node, None)
            elif node.left is None:
                self.__reassign_node(node, node.right)
            elif node.right is None:
                self.__reassign_node(node, node.left)
            else:
                tmp = self.get_max(node.left)
                self.remove(tmp.data)
                node.data = tmp.data

    def get_max(self, node):
        if node is None:
            node = self.root
        else:
            while node.right is not None:
                node = node.right
        return node

# 递归实现前序遍历
    def per_order(self, node):
        if node is None:
            return
        print(node.data)
        self.per_order(node.left)
        self.per_order(node.right)
        return node

#递归实现中序遍历
    def zhon_order(self, node):
        if node is None:
            return
        self.zhon_order(node.left)
        print(node.data)
        self.zhon_order(node.right)
        return node

# 递归实现 后续遍历
    def hou_order(self, node):
        if node is None:
            return
        self.hou_order(node.left)
        self.hou_order(node.right)
        print(node.data)
        return node
    # 前序遍历 栈实现
    def pre_ordor_stack(self,node):
        stack=[]
        while node or len(stack)>0:
            while node :
                print(node.data)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
    # 中序便利栈实现
    def cen_ordor_stack(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node.data)
                # node=self.search(node)
                node=node.right
    # 后序遍历 栈实现
    def hou_order_stack(self,node):
        if node is None:
            return False
        stack1=[]
        stack2=[]
        stack1.append(node)
        while stack1:
            node=stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().data,end="  ")
    # 层序遍历
    def level_ordor(self,root:Node):
        from queue import Queue
        queue=Queue()
        queue.put(root)
        while not queue.empty():
            node =queue.get()
            print(node.data)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

bst = BST().insert(1,2,3,4,5,6,7)
bst.zhon_order(bst.root)
bst.cen_ordor_stack(bst.root)
bst.hou_order_stack(bst.root)
bst.level_ordor(bst.root)
# if __name__ == '__main__':
# bst = BST().insert(8, 3, 6, 1)
# print(bst)
# bst.search(3)
# bst.remove(6)
# print(bst)
# bst.per_order(bst.root)
# bst.hou_order(bst.root)
# bst.zhon_order(bst.root)
