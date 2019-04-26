# -*- coding:utf-8 -*-

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        def getNext(p):
            ne=[-1]*len(p)
            j = 0
            k = -1
            while (j < len(p) - 1):
                if (k == -1 or p[k] == p[j]):
                    j+=1
                    k+=1
                    ne[j] = k
                else:
                    k = ne[k]
            return ne
        def KMP(s,p):
            ne=getNext(p)
            i=0
            j=0
            while (i < len(s) and j < len(p)):
                if (j == -1 or s[i] == p[j]):
                    i+=1
                    j+=1
                else:
                    j = ne[j]
            if (j == len(p)):
                return True
            else:
                return False


        def getN(N):
            n=''
            while(N > 0):
                if(N%2==0):
                    n='0'+n
                else:
                    n='1'+n
                N//=2
            return n
        return all(KMP(S,getN(i)) for i in range(N, N / 2, -1))

    def can_be_number(self, S, rs):
        if len(S) == 0:
            return rs
        elif len(S) == 1:
            rs.add(int(S, 2))
            return rs
        else:
            left_S = S[1:]
            right_S = S[0:len(S) - 1]
            rs.add(int(left_S, 2))
            rs.add(int(right_S, 2))
            rs.union(self.cache_number(left_S, rs))
            rs.union(self.cache_number(right_S, rs))
        return rs

    def cache_number(self, S, rs):
        if self.cache.get(S) is None:
            rsu = self.can_be_number(S, rs)
            self.cache[S] = rsu
        return self.cache[S]

    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                return ret

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.queryString("0110", 3)
    print s.queryString("0110", 4)
    print s.queryString("110101011011000011011111000000", 15)
    print s.queryString(
        "11100000011101000000101010000100001001100000000101100011101101010100011010101100010010001001100101100011011110101011000110011011101110000111100001111111000101011110110101110110101001011010100110001001",10)
