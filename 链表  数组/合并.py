from typing import List
class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        cur=self.head
        for _ in range(index):
            cur=cur.next
        return cur
    def insert(self,index,element):
        new_node=Node(element)

        if index < 0 or index> self.size:
            raise Exception('索引越界')
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node

        elif index==0:
            new_node.next=self.head
            self.head=new_node
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        else:
            pre=self.get(index-1)
            new_node.next=pre.next
            pre.next=new_node
        self.size+=1
    def remove(self,index):
        if index<0 or index>=self.size:
            raise Exception('索引越界')
        if index==0:
            remove_node=self.head
            self.head=self.head.next

        elif index==self.size-1:
            pre=self.get(index-1)
            remove_node=pre.next
            pre.next=None
            self.tail=pre
        else:
            pre = self.get(index - 1)
            remove_node = pre.next
            pre.next=pre.next.next
        self.size-=1
        return remove_node.data
    def reverse(self):
        pre =None
        cur=self.head
        while cur:
            temp=cur.next
            if pre is None:
                cur.next=pre
            else:
                cur.next=pre
            pre=cur
            cur=temp
        self.head=pre




    def __repr__(self):
        cur=self.head
        str1=""
        while cur :
            str1=str1+f"{cur}->"
            cur=cur.next
        return   str1+"END"

    def print_list(self):  # 链表内容打印
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == '__main__':
    l=LinkList()
    l.insert(0,1)
    l.insert(1,2)
    l.insert(2,4)
    l.insert(1,5)
    l.remove(3)
    # l.reverse()
    l.print_list()
    print(l)

