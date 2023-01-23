//
// Created by ryan javid on 2021-05-27.
//
#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
#define int long long
main() {
    int n; cin >> n;
    int diffrence_array[10000000];
    int array[10000000];
    int x; int y; cin >> x; cin >> y;
    int R; cin >> R;
    int sum = 0;
    for(int i = 0; i < R; i++)
    {
        int l; int r; cin >> l; cin >> r;
        diffrence_array[l]++;
        diffrence_array[r+1]--;
    }
    for(int i = 0; i < n; i++)
    {
        if(i == 0)
        {
            array[i] = diffrence_array[i];
        }
        else{
            array[i] = diffrence_array[i] + array[i-1];
        }
    }
    for(int i = x; i <= y; i++)
    {
        sum+=array[i];
    }
    cout << sum;
}