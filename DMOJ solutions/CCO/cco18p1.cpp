#include <bits/stdc++.h>
using namespace std;
#define mx 1005
    int N;
    char S[mx], T[mx];    int A[mx], B[mx];
int dp[mx][mx];
int pnt(int i, int j){
    if (A[i] < B[j]){
        if (S[i] == 'L' && T[j] == 'W'){
            return A[i]+B[j];
        }
        return 0;
    }
    if (A[i] > B[j]){
        if (S[i] == 'W' && T[j] == 'L'){
            return A[i]+B[j];
        }
        return 0;
    }
    return 0;
}
main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N;
    string temp;
    cin >> temp;
    for (int i = 1; i<=N; i++){
        S[i] = temp[i-1];
    }
    for (int i = 1; i<=N; i++){
        cin >> A[i];
    }
    cin >> temp;
    for (int i = 1; i<=N; i++){
        T[i] = temp[i-1];
    }
    for (int i = 1; i<=N; i++){
        cin >> B[i];
    }
    for (int i = 1; i<=N; i++){
        for (int j = 1; j<=N; j++){
            dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]+pnt(i, j));
        }
    }
    cout << dp[N][N];
}