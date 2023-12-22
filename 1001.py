#题目介绍
# 输入两个整数a,b输出它们的和  数据大小 (|a|,|b|<=10e9)

# 输入格式两个以空格分开的整数。(重点)
# 输出格式一个整数

# 对于比较简答的问题可以不使用函数
# 源代码
def AandB(s:str)->int:
    #将输入的字符串按照空格分开
    s=s.split()
    a=int(s[0])
    b=int(s[1])
    return a+b
s=input()
print(AandB(s))


# 题目补充字符串的split用法,默认为空格。切分后为列表。
# s="11 12 13"
# print(s.split())