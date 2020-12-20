/*
递归思路
用s, p 的下标i, j做匹配

分三种情况
1 j后跟 * 这时需要 检查s中匹配多少个j 才是合适的 

2 i j 匹配 包含 j 为'.'的情况

3 不匹配

边界情况处理
j越界时才直接返回
检查j后跟 * 时需要注意越界
检查s中匹配多少个j时需要注意 i不能越界
*/

func isMatch(s string, p string) bool {
    return helper(s, p, 0, 0)
}

func helper(s string, p string, i int, j int) bool {
        var m, n int = len(s), len(p)

        if j < n {
            
            if j != n - 1 && p[j + 1] == '*' {
                
                for {
                    if(helper(s, p, i, j + 2) == true){
                        return true
                    }

                    if i != m && (s[i] == p[j] || p[j] == '.') {
                        i = i + 1
                    } else {
                        return false
                    }
                }
                
            } else if i != m && (s[i] == p[j] || p[j] == '.') {
                return helper(s, p, i + 1, j + 1)
            } else {
                return false
            }
        }

        return i == m && j == n
}