#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> WaitInLine(vector<int>& a, vector<int>& b) {
	// write code here
	int n = a.size();
	vector<float> f;
	vector<int> ans;

	for (int i = 0; i < n; i++) {
		float t = float(a[i]) / b[i];
		f.push_back(t);
		ans.push_back(i + 1);
	}

	for (int i = 0; i < n; i++) {

		float mi = f[0];
		int order = 0;

		for (int j = 0; j <= n - 1 - i; j++) {
			if (f[j] < mi) {
				mi = f[j];
				order = j;
			}
		}

		float tmp1 = f[order];
		f[order] = f[n - 1 - i];
		f[n - 1 - i] = tmp1;

		int tmp2 = ans[order];
		ans[order] = ans[n - 1 - i];
		ans[n - 1 - i] = tmp2;

	}

	return ans;
}
