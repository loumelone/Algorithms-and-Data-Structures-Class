class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = ""
        for i in range(len(s) - 1):
           sub = self.find_longest_sub_from(i, s, sub)
        return sub 

    def find_longest_sub_from(self, n, s, sub):
        new_sub = self.find_new_sub(n, s, sub)
        if sub == "": 
            return new_sub
        if len(new_sub) > len(sub): 
            return new_sub
        return sub

    def find_new_sub(self, n, s, sub): 
        new_sub = s[n]
        if n+1 <= len(s):
            for i in range(n+1, len(s)):
                if s[i] not in new_sub:
                    new_sub += s[i]
                else: 
                    return new_sub
        return new_sub

x = Solution() 
string = "abccfg"
print(x.lengthOfLongestSubstring(string))