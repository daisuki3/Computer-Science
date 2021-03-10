#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<unordered_map>
#include<set>
//#include<stack>
//#include<set>
//#include<algorithm>
//#include<math.h>
using namespace std;

//第1行 n
//第i行 xli yli xri yri

/*
分为行和列两个子问题
转化问题 n个不同整数 第i个点必须在[li, ri]之内


错误 -》 把区间以li为基准进行排序，从坐标1至n依次分配车的位置。

应该以ri为基准进行排序！！因为坐标是从小到大进行贪心分配的。
以ri为基准才是正确的贪心策略，首先满足ri小的车是最优的。
*/
bool placeDimension(vector<vector<int>> X, vector<vector<int>>& Index) {
    int n = X.size();
    set<int> placed;

    for (int i = 0; i < n; i++) {
        //因为是从小坐标到大坐标 进行贪心放置 
        //每一轮找到右边界最小的车进行放置，防止大边界的车占用了小边界的位置
        int min = -1;
        for (int j = 0; j < n; j++) {
            if (min == -1 || X[j][1] < X[min][1]) {
                if (X[j][1] == -1) {
                    continue;
                }
                min = j;
            }
        }

        int where = X[min][0];
        while (placed.find(where) != placed.end() && where <= X[min][1]) {
            where++;
        }

        if (where > X[min][1]) {
            return false;
        }
        else {
            X[min][1] = -1;
            placed.insert(where);
            Index[min].push_back(where);
        }
    }

    return true;
}

void placeRooks(vector<vector<int>> X, vector<vector<int>> Y) {
    int n = X.size();
    vector<vector<int>> Index(n);

    if (placeDimension(X, Index) && placeDimension(Y, Index)) {
        for (int i = 0; i < n; i++) {
            cout << Index[i][0] << " " << Index[i][1] << endl;
        }
    }
    else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int n;

    while (cin >> n && n) {
        vector<vector<int>> X(n);
        vector<vector<int>> Y(n);

        for (int i = 0; i < n; i++) {
            int xl, xr, yl, yr;
            cin >> xl >> yl >> xr >> yr;
            X[i].push_back(xl);
            X[i].push_back(xr);

            Y[i].push_back(yl);
            Y[i].push_back(yr);
        }

        placeRooks(X, Y);
        X.clear();
        Y.clear();
    }
}