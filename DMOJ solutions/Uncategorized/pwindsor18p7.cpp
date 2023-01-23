#include <bits/stdc++.h>
using namespace std;
bool comp(string a, string b){
    return a+b > b+a;
}
int main(){
    int n;
    cin >> n;
    vector<string> nums;
    for (int i = 0; i<n; i++){
        string porn;
        cin >> porn;
        nums.push_back(porn);
    }
    sort(nums.begin(), nums.end(), comp);
    for (string s: nums) cout << s;
}