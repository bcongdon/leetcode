class Solution(object):
    def primeGenerator(self, n):
        l = [True] * n
        l[0], l[1] = False, False
        num_p = 0
        for n, p in enumerate(l):
            if p:
                num_p += 1
                for i in xrange(n**2, len(l), n):
                    l[i] = False
        return num_p

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        return self.primeGenerator(n)
