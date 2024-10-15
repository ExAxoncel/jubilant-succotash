class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = {}
        for char in p:
            m[char] = m.get(char, 0) + 1
        k = len(p)
        ans = []
        if len(s) < k:
            return ans
        temp = {}
        for i in range(k):
            temp[s[i]] = temp.get(s[i], 0) + 1
        if m == temp:
            ans.append(0)
        left = 0
        for i in range(k, len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1
            if temp[s[left]] == 1:
                del temp[s[left]]
            else:
                temp[s[left]] -= 1
            left += 1
            if m == temp:
                ans.append(left)
        return ans
