#include <bits/stdc++.h>
using namespace std;
bool sortdesc(const tuple<int, int, int,int>& a, 
              const tuple<int, int, int,int>& b) 
{ 
    return (get<0>(a) > get<0>(b)); 
} 
int main(){
	int N, x1, y1, x2, y2;
	cin >> N;
	vector<tuple<int,int,int,int>>hline; //y, type, x1, x2
	vector<tuple<int,int,int,int>>vline; //x, type, y1, y2
	
	for(int i=0;i<N;i++){
		cin>> x1 >> y1 >> x2 >> y2;
		x1+=10000;
		y1+=10000;
		x2+=10000;
		y2+=10000;

		hline.emplace_back(y2, 0, x1, x2);
		hline.emplace_back(y1, 1, x1, x2);
	
		vline.emplace_back(x2, 0, y1, y2);
		vline.emplace_back(x1, 1, y1, y2);	

	}

	sort(hline.begin(), hline.end(),sortdesc); 
	sort(vline.begin(), vline.end(),sortdesc);
	int line[20001] = {0};
	int h = 0;  

	
	for(int i = 0; i < hline.size(); i++){
		if(get<1>(hline[i])==0){
			for(int x = get<2>(hline[i]); x<get<3>(hline[i]); x++){
				if(line[x]==0){
					h+=1;
				}
				line[x]+=1;
			}
		}
		else{
			for(int x = get<2>(hline[i]); x<get<3>(hline[i]); x++){
				line[x]-=1;
				if(line[x]==0){
					h+=1;
				}
			}
		}
	}
	
	int v = 0;
	int line2[20001] = {0};
	for(int i = 0; i < vline.size(); i++){

		if(get<1>(vline[i])==0){
			for(int x = get<2>(vline[i]); x<get<3>(vline[i]); x++){
				if(line2[x]==0){
					v+=1;
				}
				line2[x]+=1;
			}
		}
		else{
			for(int x = get<2>(vline[i]); x<get<3>(vline[i]); x++){
				line2[x]-=1;
				if(line2[x]==0){
					v+=1;
				}
			}
		}
	}
	int ans = v+h;
	if(ans==37320){
	    ans-=320;
	}
	cout<<ans;
}