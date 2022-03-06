from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left,right = [0]*n,[0]*n
        for i in range(1,n):
            left[i] = left[i-1]+1 if security[i]<=security[i-1] else 0                          # 记录第i天前的连续非递增天数
            right[n-i-2] = right[n- i - 1] + 1 if security[n-i-2] <= security[n- i - 1] else 0  # 记录到n-i-2天后的连续非递减天数
        return [i for i in range(time,n-time) if left[i]>=time and right[i]>=time]              # 第i天同时满足left[i]>=time and right[i]>=time
                                                                                                # 则满足打劫要求

    def goodDaysToRobBank2(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        g, a, b = [0] * n, [0] * n, [0] * n
        for i in range(1, n):
            if security[i] == security[i - 1]:
                g[i] = 0
            else:
                g[i] = 1 if security[i] > security[i - 1] else -1    # 1表示递增，-1表示递减
            a[i] = a[i - 1] + (1 if g[i] == 1 else 0)                # 记录i之前的递增天数
            b[i] = b[i - 1] + (1 if g[i] == -1 else 0)               # 记录i之后的递减天数
        return [i for i in range(time, n - time) if a[i] - a[i - time] == 0 and b[i + time] - b[i] == 0]

if __name__ == '__main__':
    security = [1,1,1,1,1]; time = 0
    s = Solution()
    print(s.goodDaysToRobBank2(security, time))