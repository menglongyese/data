class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"
class LinkList:
    def __init__(self):
        self.head=None
        self.size=0
    def __repr__(self):
        cur=self.head
        res=""
        while cur:
            res=res+f"{cur}-->"
            cur=cur.next
        return res +"END"
    def get(self,index):
        if index<0 or index>self.size:
            raise Exception('索引越界')
        if self.head is None:
            raise Exception('空链表')
        else:
            cur=self.head
            for _ in range(index):
                cur=cur.next
            return cur
    def insert(self,index,data):
        new_node=Node(data)
        if self.head is None :
            self.head=new_node
        else:
            if  index==0 :
                new_node.next=self.head
                self.head=new_node
            else:
                pre_node=self.get(index-1)
                temp=pre_node.next.next
                pre_node.next=new_node
                new_node.next=temp
        self.size+=1
    def remove(self,data):
        temp=Node(0)
        temp.next=self.head
        self.head=temp
        cur=self.head
        while cur.next:
            if cur.next.data==data:
                cur.next=cur.next.next
            else:
                cur=cur.next
        self.head=self.head.next

if __name__ == '__main__':
    ll=LinkList()
    ll.insert(0,1)
    ll.insert(0, 2)
    ll.insert(0, 6)
    ll.insert(0, 3)
    ll.insert(0, 4)
    ll.insert(0, 6)
    ll.get(0)
    print(ll.get(2))
    print(ll)
    ll.remove(6)
    print(ll)






