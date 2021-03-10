#include<iostream>
#include<vector>
#include<string>
#include<sstream>
//#include<unordered_map>
//#include<stack>
//#include<set>
//#include<algorithm>
//#include<math.h>
using namespace std;

void flapjacks(int* A, int n) {
    vector<int> ans;
    int next_position = n - 1;
    while (next_position > 0) {
        int max = 0;
        for (int i = 0; i <= next_position; i++) {
            if (A[i] > A[max]) {
                max = i;
            }
        }

        //max已经在合适的位置
        if (max == next_position) {
            next_position--;
            continue;
        }

        if (max != 0) {
            int left = 0;
            int right = max;
            while (left < right) {
                int tmp = A[left];
                A[left] = A[right];
                A[right] = tmp;
                left++;
                right--;
            }
            ans.push_back(n - max);
        }
        //现在max翻转到了 index 0
        int left = 0;
        int right = next_position;
        while (left < right) {
            int tmp = A[left];
            A[left] = A[right];
            A[right] = tmp;
            left++;
            right--;
        }
        ans.push_back(n - next_position);

        next_position--;
    }

    ans.push_back(0);

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int main() {
    int A[31];
    
    vector<int> ans;
    string s;
    while (getline(cin, s)) {
        cout << s << endl;
        stringstream ss;
        ss << s;
        int i = 0;
        while (ss >> A[i]) {
            i++;
        }
        flapjacks(A, i);
        ans.clear();
    }
}