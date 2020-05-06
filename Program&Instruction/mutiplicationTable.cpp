#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;
#define len 10

int main()
{
	string str;
	int a[len][len][3];
	char b[len];
	int i, j, k, t, size;
	cin >> str;

	size = str.size();

	
	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			for (k = 0; k < 3; k++)
			{
				a[i][j][k] = 0;//初始化aij为0
			}
		}

		a[i][i][str[i] - 'a'] = 1;
		//初始化一个长度的aij等于其字符，即a[i][i][0]=‘a’=1
	}


	for (k = 1; k < size; k++)
	{
		for (i = 0; i < size && i + k < size; i++)
		{
			j = i + k;
		
			for (t = i; t < j; t++)
			{

				a[i][j][0] += a[i][t][0] * a[t + 1][j][2] + a[i][t][1] * a[t + 1][j][2] + a[i][t][2] * a[t + 1][j][0];
				a[i][j][1] += a[i][t][0] * a[t + 1][j][0] + a[i][t][0] * a[t + 1][j][1] + a[i][t][1] * a[t + 1][j][1];
				a[i][j][2] += a[i][t][1] * a[t + 1][j][0] + a[i][t][2] * a[t + 1][j][1] + a[i][t][2] * a[t + 1][j][2];
			}
		}
	}
	cout << a[0][size - 1][0] << endl;
	return 0;
}
