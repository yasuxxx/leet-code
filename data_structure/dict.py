from collections import defaultdict

# defaultdict
# map = {'c':{1},'a':{2},'b':{3}}
# m2 = defaultdict(int)
# m3 = defaultdict(str)
# m4 = defaultdict(dict)
# print(m2[2])
# print(m3[2])
# print(m4[2])

# 效果和 m in map.keys()类似
# for m in map:
#     print(m)
#
# for m in map.keys():
#     print(m)

#lambda test  元组形式实现二阶排序
# words = ['appae','appbe','appce','app','ap','a']
# words.sort(key=lambda x:(-len(x),x))
# print(words)