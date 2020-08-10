#include<iostream>
#include<stack>
#include<vector>
using namespace std;

vector<int> get(int R, int N) {
	vector<int> ans;
	vector<int> e;

	int a;
	int tmp = 0;

	while (R >= N) {

		a = R % N;
		R /= N;

		if (a == 1) {
			ans.push_back(tmp);
			tmp++;
		}
		else if (a == 0) {
			tmp++;
		}
		else
			return e;			
	}
	
	if (R == 1)
		ans.push_back(tmp);
	else
		return e;

	return ans;
}