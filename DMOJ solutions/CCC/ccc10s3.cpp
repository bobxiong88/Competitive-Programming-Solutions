#include <bits/stdc++.h>
using namespace std;
#define mx 1000000
int psa[mx];
vector<int> arr;
int get(int i, int j){
    if (j < mx){
        if (!i) return psa[j];
        else return psa[j]-psa[i-1];
    }
    else
        return psa[j-mx]+psa[mx-1]-psa[i-1];
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int H, k, m, l, r, cnt, s, curr, ans, x;
    cin >> H;
    for(int i = 0; i<H; i++){
        cin >> x;
        arr.push_back(x);
        psa[x] = 1;
    }
    cin >> k;
    sort(arr.begin(), arr.end());
    for (int i = 1; i<mx; i++){
        psa[i] += psa[i-1];
    }
    l = 0;
    r = 500000;
    ans = mx;
    while (l <= r){
        m = (l+r)/2;
        x = mx;
        for (int i = 0; i<H; i++){
            queue<int> houses;
            for (int j = i; j<H; j++){
                houses.push(arr[j]);
            }
            for (int j = 0; j<i; j++){
                houses.push(arr[j]);
            }
            s = 0;
            cnt = 0;
            while(!houses.empty()){
                curr = houses.front(); houses.pop();
                if (cnt) cnt--;
                else{
                    cnt = get(curr+1, curr+m*2);
                    s++;
                }
            }
            x = min(s, x);
        }
        if (x > k)
            l = m+1;
        else{
            r = m-1;
            ans = min(ans, m);
        }
    }
    cout << ans;
    return 0;
}