/*
nums[i] == nums[i + 1]时
用循环删掉所有nums[i + 1] == nums[i + 2]的i + 2
注意边界情况的处理，删除元素后减少size
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0; i < n; i++){
            if(i + 1 < n && nums[i + 1] == nums[i]){
                while(i + 2 < n && nums[i + 2] == nums[i]){
                    nums.erase(nums.begin() + i + 2);
                    n -= 1;
                }
            }
        }

        return nums.size();
    }
};