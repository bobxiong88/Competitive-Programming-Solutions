#include <iostream>
using namespace std;

bool lose(bool win[31][31][31][31], int a, int b, int c, int d){
	if (a < 0 || b < 0 || c < 0 || d < 0)
	    return false;
	else
	    return !win [a] [b] [c] [d];
}


int main(void){
	bool win[31][31][31][31];
	int moves[5][4] = {{2, 1, 0, 2}, {1, 1, 1, 1}, {0, 0, 2, 1}, {0, 3, 0, 0}, {1, 0, 0, 1}};
	for (int i = 0 ; i < 31 ; i++){
		for (int j = 0 ; j < 31 ; j++){
			for (int k = 0 ; k < 31 ; k++){
		    	for (int l = 0 ; l < 31 ; l++){
					win [i] [j] [k] [l] = false;
				}
			}
		}
	}
	for (int i = 0 ; i < 31 ; i++){
		for (int j = 0 ; j < 31 ; j++){
			for (int k = 0 ; k < 31 ; k++){
		    	for (int l = 0 ; l < 31 ; l++){
		    		for (int m = 0 ; m < 5 ; m++){
			    		if (lose (win,i - moves [m] [0], j - moves [m] [1], k - moves [m] [2], l - moves [m] [3])){
							win [i] [j] [k] [l] = true;
						}
					}
					
				}
			}
		}
	}
	int n,a,b,c,d;
	cin >> n;
	for (int i =0; i<n;i++){
		cin>>a>>b>>c>>d;
		if(win[a][b][c][d]){
			cout<<"Patrick"<<endl;
		}
		else{
			cout<<"Roland"<<endl;
		}
	}
	return 0;
		
	
}