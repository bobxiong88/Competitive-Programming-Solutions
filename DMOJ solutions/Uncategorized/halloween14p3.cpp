#include <bits/stdc++.h>
using namespace std;
using ll = long long;
//#define int ll
//typedef __int128 big;
#define mx 5005
string S;
ll p1, m1, a1, p2, m2, gay, a2;
ll L;
int t1[mx];
int hs[mx][mx][2];
int t2[mx];
ll v(char c){
    return int(c)-96;
}
string sub(int s, int e){
    string res = "";
    for (int i = s; i<=e; i++){
        res = res + S[i];
    }
    return res;
}
vector<vector<int>> bucket(200003);
main(){
    //freopen("input.txt", "r", stdin);
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    p1 = 31; m1 = 1e9+7;
    p2 = 51; m2 = 200003;
    cin >> S;
    L = S.length();
    t1[0] = 1;
    t2[0] = 1;
    for (int i = 1; i<mx; i++){
        t1[i] = (t1[i-1]*p1)%m1;
    }
    for (int i = 1; i<mx; i++){
        t2[i] = (t2[i-1]*p2)%m2;
    }
    for (int i = 0; i<L; i++){
        a1 = 0;
        a2 = 0;
        for (int j = i; j<L; j++){
            a1 = (a1 + v(S[j])*t1[j-i])%m1;
            hs[i][j][0] = a1;
            a2 = (a2 + v(S[j])*t2[j-i])%m2;
            hs[i][j][1] = a2;
        }
    }
    for (int i = 0; i<L; i++){
        for (int x = 1; x<L; x++){
            for (int j = x+i; j+x-1<L; j+=x){
                if (hs[i][x+i-1][0] == hs[j][j+x-1][0]){
                    gay = hs[i][j+x-1][1];
                    if (!count(bucket[gay].begin(),bucket[gay].end(), hs[i][j+x-1][0])){
                        bucket[gay].push_back(hs[i][j+x-1][0]);
                    }
                }
                else{
                    break;
                }
            }
        }
    }
    int ans = 0;
    for (int i = 0; i<m2; i++){
        ans += bucket[i].size();
    }
    cout << ans;
}