
def chu_first():
    str1=input('请输入一个数组(“,”隔开每个元素)：')

    list1=str1.split(",")
    list2=[]
    for i in list1:
        i=int(i)
        j=int(list1[0])
        shang = i / j
        list2.append(shang)
    # print(list2)
    return list2

print(chu_first())