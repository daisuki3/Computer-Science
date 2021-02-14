class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if len(s) == 0:
            return [""]
        self.ans = set()
        extra_left , extra_right = 0, 0

        for i in s:
            if i == '(':
                extra_left += 1
            elif i ==')':
                if extra_left > 0:
                    extra_left -= 1
                else:
                    extra_right += 1
        extra_total = extra_left + extra_right
        self.dfs(s, 0, extra_left, extra_right)
        return list(self.ans)
    
    def dfs(self, s, start_index, extra_left, extra_right):
        if extra_left == 0 and extra_right == 0:
                self.ans.add(s)
        for i in range(start_index, len(s), 1):
            if s[i] != '(' and s[i] != ')':
                continue

            if s[i] == '(' and extra_left > 0:
                extra_left -= 1
            elif s[i] == ')' and extra_right > 0:
                extra_right -= 1
            else:
                continue

            newS = s[:i] + s[i + 1:] 

            if extra_left == 0 and extra_right == 0:
                if self.validParenthesis(newS) == True:
                    self.ans.add(newS)
            else:
                self.dfs(newS, i, extra_left, extra_right)

            if s[i] == '(':
                extra_left += 1
            elif s[i] == ')':
                extra_right += 1

    def validParenthesis(self, s):
        left_parenthesis_num = 0
        
        for i in s:
            if i == '(':
                left_parenthesis_num += 1
            elif i == ')':
                left_parenthesis_num -= 1
                if left_parenthesis_num < 0:
                    return False
        
        return left_parenthesis_num == 0