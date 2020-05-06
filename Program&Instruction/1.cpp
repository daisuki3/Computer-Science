#include<iostream>
#include<stack>
using namespace std;

int main() {
	char a;
	stack<char> s;
	int ok, left, right;
	ok = left = right = 0;

	while (cin >> a) {

		if (a == '(' ) {
			s.push(a);
		}

		else if (a == ')') {
			if (!s.empty()) {
				char tmp = s.top();

				if (tmp == '(') {
					s.pop();
					ok += 1;
				}
				else {
					right += 1;
				}
			}
			else {
				right += 1;
			}
		}
	}

	while (!s.empty()) {

		s.pop();
		left += 1;
	}

	cout << ok << " " << left << " " << right << endl;

	return 0;
}