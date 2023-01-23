#include <bits/stdc++.h>

#include <string>

using namespace std;

#define mp make_pair

#define pb push_back

struct trip{

    int j;

    int x;

    int y;

};

#define mx 105

bool vis[mx];

vector<int> inzero;

vector<int> g[mx];

vector<int> order;

void top(int node){

    vis[node] = true;

    for (int n: g[node]){

        if (!vis[n]) top(n);

    }

    order.pb(node);

}

int main(){

    ios_base::sync_with_stdio(false); cin.tie(0);

    int n, m, k;

    cin >> n >> m >> k;

    vector<string> grids[k+1];

    for (int i = 0; i<k+1; i++){

        for (int x = 0; x<n; x++){

            string s;

            cin >> s;

            grids[i].pb(s);

        }

    }

    for (int i = 0; i<k+1; i++){

        for (int j = 0; j<k+1; j++){

            if (i == j) continue;

            bool pos = true;

            for (int x = 1; x<n-1; x++){

                for (int y=1; y<m-1; y++){

                    if (grids[i][x][y] != grids[j][x][y]){

                        if (grids[i][x][y]!=grids[i][x+1][y] && grids[i][x][y] != grids[i][x-1][y] && grids[i][x][y] != grids[i][x][y+1] && grids[i][x][y] != grids[i][x][y-1]&&grids[i][x][y]!=grids[j][x+1][y] && grids[i][x][y] != grids[j][x-1][y] && grids[i][x][y] != grids[j][x][y+1] && grids[i][x][y] != grids[j][x][y-1]){

                        }

                        else{

                            pos = false;

                        }

                    }

                }

            }

            if (pos){

                if (grids[i] == grids[j]){

                    if (i > j) continue;

                }

                g[i].pb(j);

            }

        }

    }

    for (int i = 0; i<k+1; i++){

        if (!vis[i]){

            inzero.pb(i);

            top(i);

        }

    }

    reverse(order.begin(), order.end());

    cout << order[0]+1 << "\n";

    vector<string>res;

    for (int t = 0; t<k; t++){

        int i = order[t];

        int j = order[t+1];

        for (int x = 1; x<n-1; x++){

            for (int y=1; y<m-1; y++){

                if (grids[i][x][y] != grids[j][x][y]){

                    if (grids[i][x][y]!=grids[i][x+1][y] && grids[i][x][y] != grids[i][x-1][y] && grids[i][x][y] != grids[i][x][y+1] && grids[i][x][y] != grids[i][x][y-1]&&grids[i][x][y]!=grids[j][x+1][y] && grids[i][x][y] != grids[j][x-1][y] && grids[i][x][y] != grids[j][x][y+1] && grids[i][x][y] != grids[j][x][y-1]){

                        //cout << 1 << " " << x << " " << y << "\n";

                        res.pb("1 "+to_string(x+1)+" " + to_string(y+1));

                    }

                }

            }

        }

        res.pb("2 "+to_string(j+1));

    }

    cout << res.size() << "\n";

    for (auto s:res){

        cout << s << "\n";

    }

}

