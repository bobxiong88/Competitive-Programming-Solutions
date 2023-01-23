#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int divide(int a, int b){
    return a/b;
}
string remove_occurrences(string s, string pattern){
    
    return s;
}
int count_occurrences(string s, string pattern){
    int n = s.length();
    int m = pattern.length();
    int c = 0;
    for (int i = 0; i<n-m+1; i++){
        int add = 1;
        for (int j = 0; j<m; j++){
            if (s[i+j]!=pattern[j]) add = 0;
        }
        c+=add;
    }
    return c;
}
vector<int> sort_array(vector<int> arr){
    sort(arr.begin(), arr.end());
    return arr;
}
int max_size_k(vector<int> arr, int k){
    int curr = 0;
    int ans = 0;
    for (int i = 0; i<k; i++){
        curr += arr[i];
    }
    ans = max(curr, ans);
    for (int i = 0; i<arr.size()-k; i++){
        curr -= arr[i];
        curr += arr[i+k];
        ans = max(ans, curr);
    }
    return ans;
}
char find_upper(char ch){
    return toupper(ch);
}
bool is_prime(int n){
    if (n == 1) return false;
    if (n == 2) return true;
    for (int i = 2; i<=sqrt(n); i++){
        if (n%i==0) return false;
    }
    return true;
}
int distinct_integers(vector<int> arr){
    set<int> pog;
    for (int k: arr){
        pog.insert(k);
    }
    return pog.size();
}
bool is_inside(int x, int y, int rx, int ry, int w, int h){
    return (x <= rx && rx <= x+w && y <= ry && ry <= y+h);
}

bool is_even(int n){
    return 1^(n%2);
}
bool is_bit_on(int bit, int num){
    return (num>>bit)&1;
}
int create_max(vector<int> dig){
    sort(dig.begin(), dig.end());
    int ans = 0;
    for (int i = 0; i < dig.size(); i++){
        ans += dig[i]*pow(10, i);
    }
    return ans;
}
int factorial(int n, int m){
    ll ans = 1;
    for (int i = 1; i<=n; i++){
        ans *= i;
        ans %= m;
    }
    return ans;
}
bool should_feed(int h, int m, int th){
    return h*m >= th;
}
    int gcd(int a, int b){
        if (a == 0) return b;
        return gcd(b%a, a);
    }
pair <int,int> lowest_terms(int num, int denom){

    int g = gcd(num, denom);
    return make_pair(num/g, denom/g);
}
int find_sum(int n){
    return (n*(n+1))/2;
}
string find_type(int type){
    if (type == 1) return "max, do";
    if (type == 2) return "dhruv, fold";
    if (type == 3) return "abayomi, open";
    if (type == 4) return "snjezana, write";
    if (type == 5) return "yuxuan, close";
    if (type == 6) return "mohamed, move";
    if (type == 7) return "scarlet, crush";
    if (type == 8) return "anastasia, tear";
    if (type == 9) return "aksana, press";
    if (type == 10) return "alejandro, cut";
}
    bool comp(string a, string b){
        return a > b;
    }
string largest_lex(vector<string> arr){

    sort(arr.begin(), arr.end(), comp);
    return arr[0];
}
vector<int> add_colours(vector<int> c1, vector<int> c2){
    for (int i = 0; i<3; i++){
        c1[i] += c2[i];
        c1[i] = max(255, c1[i]);
    }
    return c1;
}
bool AC(){
    return true;
}
int main(){
}