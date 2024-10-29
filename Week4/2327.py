class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        mod = 10**9 + 7
        v = [0] * n
        v[0] = 1
        sum = 0
        for i in range(1, n):
            if i >= forget:
                sum = (sum - v[i - forget]) % mod
            if i >= delay:
                sum = (sum + v[i - delay]) % mod
            v[i] = sum
        cnt = 0
        for i in range(n - forget, n):
            cnt = (cnt + v[i]) % mod
        return cnt
    