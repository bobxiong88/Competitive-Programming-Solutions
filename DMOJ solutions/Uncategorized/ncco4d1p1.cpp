#include <bits/stdc++.h>
using namespace std;
int main(){
    // start small
    priority_queue<int> racism;
    int x, y, N;
    cin >> N;
    while(N--){
        cin >> x;
        racism.push(-x);
    }
    long long ans = 0;
    while (racism.size()>=2){
        x = racism.top();racism.pop();
        y = racism.top();racism.pop();
        racism.push(x+y);
        ans += -(x+y);
    }
    cout << ans << "\n";
}