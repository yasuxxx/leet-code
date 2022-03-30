from collections import deque


class MonotoniQueue:

    def __init__(self):
        # 常用函数： pop popleft
        #          append appendleft
        self.queue = deque()

    def pop(self,m):
        if m==self.queue[0]:
            self.queue.popleft()


    def push(self,n):
        while self.queue and self.queue[-1]<n:
            self.queue.pop()
        self.queue.append(n)

    def max(self):
        return self.queue[0]

if __name__ == '__main__':
    # res = [4,4,4,5,5,6,6,8,8] , k = 3
    arr = [2,3,4,1,1,5,4,6,5,8,3]
    res = []
    mq = MonotoniQueue()
    for i,v in enumerate(arr):
        if i<3:
            mq.push(v)
        else:
            res.append(mq.max())
            mq.pop(arr[i-3])
            mq.push(arr[i])
    print(res)