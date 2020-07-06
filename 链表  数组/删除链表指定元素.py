class Node :
    def __init__(self,data):
        self.next=None
        self.data=data
    def __repr__(self):
        return  f"Node({self.data})"
class LinhList:
    def __init__(self):
        self.head=None
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
    def delete(self,val):
        if self is None:
            raise Exception('空链表')
        while self.head.data == val:
            self.head = self.head.next
        cur=self.head
        while cur.next:
            if cur.next.data == val:
                cur.next=cur.next.next
            else:
                cur=cur.next

    def __repr__(self):  # 链表打印
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"
if __name__ == '__main__':
    ll=LinhList()
    ll.insert_head(2)
    ll.insert_head(3)
    ll.insert_head(4)
    ll.insert_head(2)
    ll.delete(2)
    print(ll)



