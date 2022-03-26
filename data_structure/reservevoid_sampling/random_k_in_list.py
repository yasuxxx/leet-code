

# 取出数据流中的随机k个数
import random
def reserved_sampling(alist,k):
    res = []
    # 模拟数据流的输入
    for i,v in enumerate(alist):
        if i<k:res.append(v)
        else:
            # k/n的概率选择是否替换
            if random.randrange(i)<k:
                # 1/k的概率选择替换哪个数
                j = random.randrange(k)
                res[j] = v
    return res