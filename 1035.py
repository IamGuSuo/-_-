# 输入格式:一个正整数
# 输出格式 :一个正整数
# 源代码
def sum_num(k: int) -> int:
    # 初始化sn
    sn = 1
    # n的数值
    n = 1
    while True:
        if sn > k:
            return n
        sn += 1 / (n + 1)  # sn=sn+(1/(n+1)) 的简写
        n += 1


k = int(input())
print(sum_num(k))

# 题目补充:没有技术含量，只是简单的处理一些问题。
