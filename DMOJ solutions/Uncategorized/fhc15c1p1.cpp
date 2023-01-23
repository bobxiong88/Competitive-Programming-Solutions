#include <bits/stdc++.h>
using namespace std;
int main(){
	int N[10000001] = {0};
	N[0] = 0;
	N[1] = 0;
	for(int i = 2; i<10000001; i++){
		if (N[i] == 0){
			for(int j = i; j<10000001; j+=i){
				if (j<10000001)
					N[j]++;
			}
		}
	}
	int T, A, B, K, ans;
	cin >> T;
	for(int i=1;i<=T;i++){
		cin >> A >> B >> K;
		ans = 0;
		for(int i = A; i<=B; i++){
			if(N[i]==K){
				ans++;
			}
		}
		cout << "Case #"<< i <<": " << ans << "\n";
	}
	
}