/*
对于每个点，往后遍历到尾
统计斜率为k的直线的点数
统计重复点
从这个点开始往后的最长直线为 1 + 重复点 + 最长的直线

注意斜率的精度用long double存储斜率并把斜率乘以10000提高精度
注意此时dy dx要用long long存储防止越界
*/
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        /*
        if(points.size() < 3){
            return points.size();
        }
        */

        int ans = 0;
        for (auto P = points.begin(); P != points.end(); P++) {
            int dup = 0;
            unordered_map<long double, int> num_of_slope = {
                {FLT_MAX, 1}
            };
            int tmp_res = 0;
            long long px = (*P)[0];
            long long py = (*P)[1];

            for (auto Q = P + 1; Q != points.end(); Q++) {
                auto qx = (*Q)[0];
                auto qy = (*Q)[1];
                if (px == qx && py == qy) {
                    dup++;
                }
                else if (px == qx) {
                    num_of_slope[FLT_MAX] += 1;
                    tmp_res = max(tmp_res, num_of_slope[FLT_MAX]);
                }
                else {
                    long long dy = qy - py;
                    long long dx = qx - px;
                    long double slope = static_cast<long double> (dy * 10000) / dx;
                    if (num_of_slope.find(slope) == num_of_slope.end()) {
                        num_of_slope[slope] = 2;
                    }
                    else {
                        num_of_slope[slope] += 1;
                    }
                    tmp_res = max(tmp_res, num_of_slope[slope]);
                }
            }
            if (tmp_res == 0) {
                ans = max(ans, dup + 1);
            }
            else {
                ans = max(ans, tmp_res + dup);
            }
        }
        return ans;
    }
};