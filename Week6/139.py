class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        dp = {}

        def solve(substr):
            if not substr:
                return True

            if substr in dp:
                return dp[substr]

            for i in range(len(substr)):
                prefix = substr[:i + 1]

                if prefix in word_set and solve(substr[i + 1:]):
                    dp[substr] = True
                    return True

            dp[substr] = False
            return False

        return solve(s)
