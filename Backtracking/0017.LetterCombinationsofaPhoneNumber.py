'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = "2"
    Output: ["a","b","c"]
'''
def letterCombinations(self, digits: str) -> list[str]: #T: O(4ⁿ) S: O(n)
    res = []
    digit2char = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def backtrack(idx, cur_str):
        if len(cur_str) == len(digits):
            res.append(cur_str)
            return
        for c in digit2char[digits[idx]]:
            backtrack(idx+1, cur_str+c)
    if digits:
        backtrack(0,"")
    return res