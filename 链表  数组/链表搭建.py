from typing import List


class Node:  # 节点创建
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:  # 链表创建
    def __init__(self):
        self.head = None

    def insert_head(self, data):  # 头部插入
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):  # 尾部插入
        if self.head is None:
            self.insert_head(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert(self, i, data):  # 中间插入
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data)
            cur = self.head
            pre = cur

            j = 1
            while j < i:
                pre = cur
                cur = cur.next
                j += 1
            pre.next = new_node
            new_node.next = cur

    def linklist(self, obj: List):  # 列表转化为链表
        new_node = Node(obj[0])
        self.head = new_node
        cur = self.head
        for i in obj[1:]:
            cur.next = Node(i)
            cur = cur.next
    def linklist(self,i,obj:List):
        # new_node=Node(obj[0])

        cur=self.head
        if cur is None or i==1:
            for i in obj[0:]:
                cur.next=Node(i)
                cur=cur.next
        else:
            pre=cur
            j=1
            while j<i:
                pre=cur
                cur=cur.next
                j+=1
            for i in obj[0:]:
                pre.next=Node(i)
                pre=pre.next
            pre.next=cur


    def delete_head(self):  # 删除头部
        cur = self.head
        if cur is None:
            print("空链表")
        else:
            self.head = cur.next

    def pop(self):  # 删除尾部方法一
        cur = self.head
        if cur is None:
            print('空链表')
        else:
            while cur.next.next is not None:
                cur = cur.next
            popf = cur.next.data
            cur.next = None
        return popf

    def pop(self):  # 删除尾部方法二
        cur = self.head
        pre = cur
        if cur is None:
            print('空链表')
        else:
            while cur.next:
                pre = cur
                cur = cur.next
            popf = cur.data
            pre.next = None
            return popf

    def print_list(self):  # 链表内容打印
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def __repr__(self):  # 链表打印
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"


if __name__ == '__main__':  # 主函数
    ll = LinkList()
    ll.linklist([1, 2, 3, 4, 5])
    ll.append("append")
    ll.insert_head(100)
    ll.insert_head("ds")
    ll.insert_head(98)
    ll.append("append")
    ll.insert(3, "insert")
    # ll.delete_head()
    # ll.pop()

    ll.print_list()
    print("=" * 30)
    print(ll)
    print(ll.pop())
