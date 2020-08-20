/**
 * 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
 * 
 * 用数组储存四段数字，第四组存完后，通过该数组得到一个答案
 * 
 * 
 * 
 * 
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    let ans = []

    let toans = []

    function re(order, start){
        
        if(order === 4){
            //是第五次且字符串刚好用完
            if(start === s.length){
                ans.push(toans.join("."))
            }
  
            return
        }

        //不是第五次但是却已经用完了字符串
        if(start === s.length){
            return
        }

        //起始位为0，这次只能取0
        if((s.charAt(start) - '0') === 0){
            toans[order] = 0
            re(order + 1, start + 1)
            return
        }
        

        let num = 0
        for(let end = start; end < s.length; end++){
            //回溯，进行下一次尝试
            num = num * 10 + (s.charAt(end) - '0')
            
            if(num <= 255){
                toans[order] = num
                re(order + 1, end + 1)
            }
        }        
    }

    re(0, 0)

    return ans
};