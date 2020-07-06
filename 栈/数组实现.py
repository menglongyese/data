class Stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    # def __bool__(self):
    #     return bool(self.stack)
    def __str__(self):
        return  str(self.stack)

    def push(self,data):
        if len(self.stack)<self.size:
            raise Exception("溢出")
        self.stack.append(data)
        self.size+=1
        # return self.stack
    def pop(self):
        if self.stack:
            popf=self.stack.pop()
            self.size-=1
            return popf
        else:
            raise Exception('空栈')
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return not bool(self.stack)
    def size1(self):
        return self.size
if __name__ == '__main__':
    st=Stack()
    print(st.is_empty())
    for i in range(10):
        st.push(i)


    print(st)
    # print(st.pop())
    print(st.peek())
    print(st.size1())

