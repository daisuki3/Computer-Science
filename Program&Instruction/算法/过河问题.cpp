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

const int boat_capacity = 3;
/*
任何时候,任何地点 num_people >= num_animal
船容量 3
初始状态 (m,n) (0,0)
目标状态 (0,0) (m,n)

操作 
左至右
m - 2 n - 1
m - 1 n - 1
m - 1
m - 2
m - 3
n - 1 
n - 2
n - 3
右至左
m + 1
n + 1

搜索？
谁来划船？同样也需要搜索。

保证船上永远是安全的
先尝试最贪心的操作，否则可能导致死循环
*/
int left_op[8][2] = {
    {-2, -1},
    {-1, -1},
    {-3, 0},
    {-2, 0},
    {-1, 0},
    {0, -3},
    {0, -2},
    {0, -1},
};

int right_op[2][2] = {
    {-1, 0},
    {0, -1}
};
vector<string> ans;
//(a, b) a : num_people b : num_animal
bool valid(int left_p, int left_a, int right_p, int right_a);
bool dfs(int left_p, int left_A, int right_p, int right_a);
void crossRiver(int num_people, int num_animal);

bool valid(int left_p, int left_a, int right_p, int right_a) {
    
    if (left_p < 0 || left_a < 0 || right_p < 0
        || right_a < 0) {
        return false;
    }

    if ((left_p != 0 && left_p < left_a) || (right_p != 0 && right_p < right_a) ) {
        return false;
    }
    else {
        return true;
    }
}

void crossRiver(int num_people, int num_animal) {
    dfs(num_people, num_animal, 0, 0);
}

bool dfs(int left_p, int left_a, int right_p, int right_a) {
    //dfs函数走一轮来回 对合适的来回选择开启下一轮dfs
    int tl_p = left_p;
    int tl_a = left_a;
    int tr_p = right_p;
    int tr_a = right_a;
    for (int i = 0; i < 8; ++i) {
        int op_1 = left_op[i][0];
        int op_2 = left_op[i][1];
        left_p += op_1;
        left_a += op_2;
        right_p -= op_1;
        right_a -= op_2;

        if (valid(left_p, left_a, right_p, right_a) == false) {
            left_p = tl_p;
            left_a = tl_a;
            right_p = tr_p;
            right_a = tr_a;
            continue;
        }

        if (left_p == 0 && left_a == 0) {
            cout << "步骤如下:" << endl;
            ans.push_back( "--- 从左往右划船 " + to_string(-left_op[i][0]) + "个传教士 " + to_string(-left_op[i][1])+ "个野兽" );
            return true;
        }

        for (int j = 0; j < 2; ++j) {
            right_p += right_op[j][0];
            right_a += right_op[j][1];
            left_p -= right_op[j][0];
            left_a -= right_op[j][1];
        
            if (valid(left_p, left_a, right_p, right_a) == false) {
                left_p = tl_p;
                left_a = tl_a;
                right_p = tr_p;
                right_a = tr_a;
                continue;
            }

            if (dfs(left_p, left_a, right_p, right_a) == true) {
                ans.push_back( "--- 从左往右划船 " + to_string(-left_op[i][0]) + "个传教士 " + to_string(-left_op[i][1]) + "个野兽  " + " --- 从右往左划船 "
                    + to_string(-right_op[j][0]) + "个传教士 " + to_string(right_op[j][1]) + "个野兽");
                return true;
            }
        }
    }

    return false;
}

int main() {
    crossRiver(3, 2) ;
    int j = 1;
    for (int i = ans.size() - 1; i >= 0; --i) {
        cout << j << " : " << ans[i] << endl;
        j += 1;
    }
}