class student:
    def __init__(self,name,age):#固有属性
        self.name= name
        self.age=age
    def study(self):#能力方法
        print("{}可以学习".format(self.name))

stu = student('lili',18)
print(stu.age)
print(stu.name)