class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        total = 0
        max_int = 2**31 - 1
        min_int = -2**31

        if s[0] == '+':
            index += 1
        elif s[0] == '-':
            sign = -1
            index += 1

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if total > (max_int - digit) // 10:
                return max_int if sign == 1 else min_int
            total = total * 10 + digit
            index += 1

        return sign * total
