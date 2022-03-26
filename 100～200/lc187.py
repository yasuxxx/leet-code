from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:return list()
        res = list()
        ss = set()
        ss.add(s[0:10])
        for i in range(10,len(s)):
            if s[i-9:i+1] in ss and s[i-10:i] not in res:
                res.append(s[i-10:i])
            ss.add(s[i-10:i])
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.findRepeatedDnaSequences("CAAAAAAAAAC")
    print(res)

