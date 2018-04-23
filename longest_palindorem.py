class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1),res,key=len)
        return res

    def helper(self,s, i, j):
        # self is important,do not forget it again
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1;
            j += 1
        return s[i + 1:j]
s = "abcddcab"
a=Solution()
print(a.longestPalindrome(s))