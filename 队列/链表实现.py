from typing import Any ,Optional
class Node :
    def __init__(self,iterm:Any):
        self.iterm:Any=iterm
        self.next:Optional = None
    def __repr__(self):
        return f"Node({self.iterm})"
class LinkQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def put(self,iterm):
        new_node=Node(iterm)
        if self.front is None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
    def pop(self):
        if self.front is None:
            raise Exception('空队列')
        else:
            popf=self.front
            self.front=self.front.next

        self.size-=1
        return popf
    def get(self,index):
        cur=self.front
        if index<0 or index>self.size:
            raise Exception('索引越界')

        for _ in range(1,index):
            cur=cur.next
        return cur
    def size1(self):
        return self.size

    def __repr__(self):
        cur = self.front
        string_repr = ""
        while cur:
            string_repr += f"{cur} --> "
            cur = cur.next
        return string_repr + "END"

if __name__ == '__main__':
    lq=LinkQueue()
    for i in range(10):
        lq.put(i)
    lq.pop()
    print(lq.get(4))
    print(lq)
    print(lq.size1())



