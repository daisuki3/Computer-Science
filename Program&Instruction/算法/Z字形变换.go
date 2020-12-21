/*
思路
row + row - 2 为一个分组
根据当前下标在分组中的位置 添加字符到ans中
共遍历numRows次，每轮遍历时，遍历字符串s，找到是分组中该位置的字符，添加到ans中 

边界情况处理 
要注意 groupNum为2时，是没有Z的，注意把此时的start添加进去，方法是把start取余
j为groupNum时，取余得到0，注意把end也取余

时间复杂度 len(s) * len(s) 空间复杂度1
上面这种思路 运行时间过长，太多无效遍历，遍历步长太小！！

可以取步长为groupNum，
这样时间复杂度为 len(s)
需要注意的是每轮循环，先后添加对应组的start end，而不是添加完所有的start再去添加end 

*/
func convert(s string, numRows int) string {

    if numRows == 1 || numRows == 0 {
        return s
    }

    var ans string = ""
    var groupNum int = numRows + numRows - 2

    for i := 1; i <= numRows; i++ {
        var start, end int = i, (groupNum + 2 - i)

        
        if i > len(s) {
            break
        }
        

        /*
        for j, v := range s {
            if (j + 1) % groupNum == start % groupNum {
                ans = ans + string(v)
            } else if end > numRows && end <= groupNum && (j + 1) % groupNum == end % groupNum {
                ans = ans + string(v)
            }
        }
        */
        var j, k int = start - 1, end - 1

        for j < len(s) || k < len(s) {

            //fmt.Println(j)

            if (j + 1) % groupNum == (start % groupNum) {
               // fmt.Println(s[j], '?')
                ans = ans + string(s[j])
            }

            if end > numRows && end <= groupNum && k < len(s) && (k + 1) % groupNum == (end % groupNum) {
                //fmt.Println(s[j], '?')
                ans = ans + string(s[k])
            }

            j += groupNum
            k += groupNum
        }
    }

    return ans
    
}