from pprint import pformat


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self is None:
            return str(self.data)
        else:
            return pformat({"%s" %
                            (self.data): (self.left, self.right)}, indent=1)


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
            cur = self.root
            while True:
                if new_node.data < cur.data:
                    if cur.left is None:
                        cur.left = new_node
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = new_node
                        break
                    else:
                        cur = cur.right
            new_node.parent = cur

    def insert(self, *list):
        for i in list:
            self.__insert(i)
        return self

    def rearch(self, data):
        if self.is_empty():
            raise Exception("空二叉树")
        else:
            cur = self.root
            while cur and cur.data != data:
                if data < cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
            print(cur)
            return cur

    def is_right(self, node):
        return node.parent.right == node

    def __reassign(self, node, newchildren):
        if newchildren is not None:
            newchildren.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = newchildren
            else:
                node.parent.left = newchildren
        else:
            self.root = newchildren

    def get_max(self, node):
        if node is None:
            return self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
            return node

    def remove(self, data):
        node = self.rearch(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign(node, None)
            elif node.left is None:
                self.__reassign(node, node.right)
            elif node.right is None:
                self.__reassign(node, node.left)
            else:
                tmp = self.get_max(node.left)
                node.data = tmp.data
                self.remove(tmp.data)

    def pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

        # return node
bst = BST().insert(8, 3, 6, 1)
# bst.pre_order(bst.root)
print(bst.pre_order(bst.root))


# if __name__ == '__main__':
#     bst=BST().insert(8,5,7,2,9,6,9)
#     # print(bst)
#     # bst.rearch(5)
#     # # print(bst.rearch(7))
#     bst.remove(7)
#     # print(bst)
