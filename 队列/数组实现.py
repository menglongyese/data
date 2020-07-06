class Queue:
    def __init__(self):
        self.entries=[]
        self.size=0
        # self.front=0
    def __str__(self):
        printed="<"+str(self.entries)[1:-1]+'>'
        return printed
    def put(self,item):
        self.entries.append(item)
        self.size+=1
    def get(self):  #出队
        dequeued=self.entries[0]
        self.size=self.size-1
        self.entries=self.entries[1:]
        return dequeued
    def fan(self):
        self.entries=self.entries[::-1]
        return self.entries

    def front(self):
        return  self.entries[0]
    def size1(self):
        return  self.size

if __name__ == '__main__':
    qu=Queue()
    for i in range(10):
        qu.put(i)
    print(qu)
    qu.get()
    print(qu)
    print(qu.size1())
    print(qu.fan())
