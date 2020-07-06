class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return  f'Node({self.data})'
def delect(head,val):
    xv=Node(1)
    xv.next=head
    cur=xv
    while cur.next:
        if cur.next.data == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return xv.next
def print_list(head):
    cur=head
    while cur :
        print(cur.data)
        cur=cur.next
# if __name__ == '__main__':

n1=Node(1)
n2=Node(2)
n3=Node(1)
n1.next=n2
n2.next=n3
delect(n1,1)

print_list(delect(n1,1))