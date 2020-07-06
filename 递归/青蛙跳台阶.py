# def jump(n):
#     if n<=2:
#         return n
#     else:
#         return jump(n-1)+jump(n-2)
# jump(3)
def jump(n):
    if n<= 2:
        return n
    return jump(n-1)+jump(n-2)

print(jump(5))