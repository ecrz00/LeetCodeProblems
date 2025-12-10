'''
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
'''
def longestCommonPrefix(self, strs: list[str]) -> str: #T: O(n), S: O(1)
    if not strs:
        return ""
    min_len = min(len(s) for s in strs)
    i=0
    while i < min_len:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i+=1
    return strs[0][:min_len]
        