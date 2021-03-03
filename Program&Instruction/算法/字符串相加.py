'''
把字符串反转然后相加
注意进位的边界处理
检查最高位是否需要进位
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        
        nums1 = num1[::-1]
        nums2 = num2[::-1]
        
        i = 0
        incre = 0
        nums = ""
        while i < n1 and i < n2:
            s = int(nums1[i]) + int(nums2[i]) + incre            
            incre = 1 if s > 9 else 0
            nums += str(s % 10)
            i += 1
        
        if i < n1:
            while i < n1:
                s = int(nums1[i]) + incre
                incre = 1 if s > 9 else 0
                nums += str(s % 10)
                i += 1
        else:
            while i < n2:
                s = int(nums2[i]) + incre
                incre = 1 if s > 9 else 0
                nums += str(s % 10)
                i += 1

        if incre == 1:
            nums += "1"
        
        return "".join(list(nums)[::-1])