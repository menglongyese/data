from pprint import pformat
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)
    return node
def pre_order_stack(node):
    stack=[]
    while node or len(stack)>0:
        while node:
            print(node.data)
            stack.append(node)
            node=node.left
        if len(stack)>0:
            node=stack.pop()
            node=node.right
