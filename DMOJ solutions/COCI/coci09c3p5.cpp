#include <bits/stdc++.h>
#include <ctime>
using namespace std;
int arr[300001];
vector <vector<int>> freq(10001);
int n, m, a, b, c;
int up(int a, int i){
    int left = 0;
    int right = freq[i].size()-1;
    if (freq[i][right] < a){
        return -1;
    }
    if (freq[i][left] >= a){
        return left;
    }
    while (left <= right){
        int middle = floor((left+right)/2);
        if (freq[i][middle-1] < a && a <= freq[i][middle]){
            return middle;
        }
        if (freq[i][middle] < a){
            left = middle + 1;
        }
        else if (freq[i][middle] > a){
            right = middle - 1;
        }
    }
}
int down(int b, int i){
    int left = 0;
    int right = freq[i].size()-1;
    if (freq[i][left] > b){
        return -1;
    }
    if (freq[i][right] <= b){
        return right;
    }
    while (left <= right){
        int middle = floor((left+right)/2);
        if (freq[i][middle] <= b && b < freq[i][middle+1]){
            return middle;
        }
        if (freq[i][middle] < b){
            left = middle + 1;
        }
        else if (freq[i][middle] > b){
            right = middle - 1;
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int k = 19;
    cin >> n >> c;
    for (int i = 1; i<=n; i++){
        cin >> c;
        arr[i] = c;
        freq[c].push_back(i);
    }
    cin >> m;
    for (int q = 0; q<m; q++){
        srand(time(NULL));
        cin >> a >> b;
        bool flagged = false;
        //cout << "for range " << a << "," << b << "\n";
        for (int x = 0; x<k; x++){
            int res = rand()%(b-a+1)+a;
            int i = arr[res];
            //cout << x << ":" << res << "\n";
            int l = up(a, i);
            int r = down(b, i);
            if (l == -1 || r == -1) continue;
            if ((r-l+1)>((b-a+1)/2)){
                flagged = true;
                cout << "yes " << i << "\n";
                break;
            }
        }
        if (!flagged) cout << "no" << "\n";
    }
}