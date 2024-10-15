class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ''
        temp = ''
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        while i < n:
            c = s[i]
            if c == ' ':
                if temp:
                    temp = temp[::-1]
                    ans += temp + ' '
                    temp = ''
                while i < n and s[i] == ' ':
                    i += 1
            else:
                temp += c
                i += 1
        if temp:
            temp = temp[::-1]
            ans += temp
        if ans and ans[-1] == ' ':
            ans = ans[:-1]
        ans = ans[::-1]
        return ans
