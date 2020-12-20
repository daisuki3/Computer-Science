/*
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。



动态规划 思路
dp[i][j] 代表 s[:i + 1] 与 p[j + 1] 是否匹配
状态转移 dp[i][j] =
if p[j] == '*'                         
dp[i - 1][j - 1] ( *匹配i ) || dp[i - 1][j] ( *匹配了i - 1 同时来匹配i) || dp[i][j - 1] (*不作匹配)

else if s[i] == p[j] || p[j] == '?'        
dp[i - 1][j - 1]

else
false

dp[0][0] true
dp[i][0]  false
dp[0][j] 1~j全为* true 其余false
*/
func isMatch(s string, p string) bool {

    dp := make([][]bool, len(s) + 1)
    
    for i := 0; i <= len(s); i++ {
        dp[i] = make([]bool, len(p) + 1)
    }

    
    for i := 0; i <= len(s); i++ {
        dp[i][0] = false
    }

    dp[0][0] = true
    for i := 1; i <= len(p); i++{
        
        if p[i - 1] == '*'{
            dp[0][i] = dp[0][i - 1]
        } else {
            dp[0][i] = false
        }
    }


    for i := 1; i <= len(s); i++ {
        for j := 1; j <= len(p); j++ {
            
            if p[j - 1] == '*' {
                dp[i][j] = dp[i - 1][j - 1] || dp[i - 1][j] || dp[i][j - 1]
            } else if s[i - 1] == p[j - 1] || p[j - 1] == '?' {
                dp[i][j] = dp[i - 1][j - 1]
            } else{
                dp[i][j] = false
            }
            
        }
    }

    //fmt.Println(dp[len(s)][len(p) - 1])
    return dp[len(s)][len(p)]
}




/*
递归超时 

func isMatch(s string, p string) bool {
    if len(p) == 0 {
        return len(s) == 0 
    }

    var newP string = string(p[0])
 
    for _, v := range p[1:] {

        if v == '*' {
            if len(newP) == 0 || newP[len(newP) - 1] !='*' {
                newP += string(v)
            }
        } else{
            newP += string(v)
        }
    }

    fmt.Println(newP)

    return helper(s, newP, 0, 0)
}

func helper(s string, p string, i int, j int) bool {
    var m, n int = len(s), len(p)

    if j < n {

        if p[j] == '*' {
            
            for {
                if helper(s, p, i, j + 1) == true {
                    return true
                }

                if i < m {
                    i = i + 1
                } else {

                    return false
                }
            }
        } else if i < m && (s[i] == p[j] || p[j] == '?') {
            return helper(s, p, i + 1, j + 1)
        } else {
            return false
        }

    }
    
    return i == m && j == n
}
*/