'''
需要考虑两种情况。
一是右括号匹配很远的左括号。
二是括号闭合之后形成连环，即形成几组连续的闭合括号。这时他们的长度之和才是有效括号长度。

每个右括号我们需要知道它所对应的左括号的下标，以得到长度
我们还要处理括号连环，所以需要标记 有效闭合的右括号 所在组的长度。

left_index_arr 存储左括号下标
group_length 存储有效闭合右括号所在组（有可能连环）的长度
dp 存储最长有效括号

'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0 
        ans = 0
        
        dp = []
        left_index_arr = []
        group_length = []

        for i in range(len(s)):
            dp.append(0)
            group_length.append(0)
            if s[i] == '(':
                left_index_arr.append(i)
                if i > 0:
                    dp[i] = dp[i - 1]
            elif s[i] == ')':
                if len(left_index_arr) != 0:
                    left_index = left_index_arr.pop()
                    length = i - left_index + 1
                    if left_index > 0 and group_length[left_index - 1] > 0:
                        group_length[i] = group_length[left_index - 1] + length
                    else:
                        group_length[i] = length
                    dp[i] = max(dp[i - 1], group_length[i])
                else:
                    if i > 0:
                        dp[i] = dp[i - 1]
        
        return dp[len(s) - 1]