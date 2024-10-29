class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        n = len(s)
        i = 0
        ans = ''
        while i < n:
            if s[i] == ']':
                op = ''
                while st:
                    if st[-1] == '[':
                        st.pop()
                        break
                    op = st.pop() + op
                ok = op
                num = ''
                while st:
                    if '0' <= st[-1] <= '9':
                        num += st.pop()
                    else:
                        break
                num = num[::-1]
                k = int(num)
                op = ''
                while k > 0:
                    op += ok
                    k -= 1
                st.append(op)
            else:
                g = ''
                g += s[i]
                st.append(g)
            i += 1
        while st:
            ans = st.pop() + ans
        return ans
    