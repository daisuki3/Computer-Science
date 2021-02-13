/*
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

思路：
给定start，当前下标大于start值时是一个盆，
可以接一波雨水，短板是start。然后更新start

最右端如果没有以start为短板的盆
说明start是高板
从末尾到start，倒序再调用一次函数
*/
class Solution {
    public int trap(int[] height) {
        int ans = 0;
        int start = 0;
        
        int max = 1;

        int sum = 0;

        for(int i = 1; i < height.length; i++){

            if(height[i] >= height[max]){
                max = i;
            }

            if(height[i] >= height[start]){
                ans += height[start] * (i - start - 1) - sum;
                
                start = i;
                sum = 0;
                max = i + 1;
            }
            else{
                sum += height[i];
            }
        }
        

        if(max < height.length){
            int len  = height.length - 1 - start + 1;

            int newArr[] = new int[len];
            
            for(int i = height.length - 1, j = 0; i >= start; i--, j++){
                newArr[j] = height[i];
            }

            ans += trap(newArr);
        }
        

        return ans;
    }
}