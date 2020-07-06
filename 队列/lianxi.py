class Queue:
    def __init__(self):
        self.list=[]
        self.size=0
    def __str__(self):
        printed="<"+str(self.list)[1:-1]+">"
        return printed
    def put(self,iterm):
        self.list.append(iterm)
        self.size+=1
    def get(self):
        res=self.list[0]