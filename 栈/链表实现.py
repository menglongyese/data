class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return  f"Node({self.data})"

class  LinkStact:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        new_st=Node(data)
        new_st.next=self.top
        self.top=new_st
        self.size+=1
    def pop(self):
        if self.top is  None:
            raise Exception('空栈')
        popf=self.top
        self.top=self.top.next
        return popf.data
    def peek(self):
        if self.top is  None:
            raise Exception('空栈')

        return self.top.data
    def is_empty(self):
        return not bool(self.top)
    def size1(self):
        return self.size

    def __repr__(self):  # 链表打印
        current = self.top
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"
if __name__ == '__main__':
    ll=LinkStact()
    print(ll.is_empty())
    for i in range(10):
        ll.push(i)
    print(ll)
    print(ll.size1())
    print(ll.pop())









