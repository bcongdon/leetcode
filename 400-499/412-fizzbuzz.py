class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out.append('FizzBuzz')
            elif i % 3 == 0:
                out.append('Fizz')
            elif i % 5 == 0:
                out.append('Buzz')
            else:
                out.append(str(i))
        return out