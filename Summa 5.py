#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;

int main()
{
	int n_max = 10;
	double sum = 0.0;
	for (int i = 1; i < n_max + 1; i++)
	{
		sum += ((3*i+1) / (2*i-1));
	}
	cout << "Summa: " << sum;
	return 0;
}
