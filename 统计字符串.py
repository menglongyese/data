def countn(s: str):
    dic = {'数字': 0, '字母': 0, '空格': 0, '其他': 0}
    for i in s:
        if i.isdigit():
            dic['数字'] += 1
        elif i.isalpha():
            dic['字母'] += 1
        elif i.isspace():
            dic['空格'] += 1
        else:
            dic['其他'] += 1
    return dic


s = input('请输入一个字符串：')
print(countn(s))




