#include <bits/stdc++.h>
using namespace std;
int deg[1505];
void initialize(int n){
}
int hasEdge(int u, int v){
    if (u<v)swap(u,v);
    if (++deg[u] == u) return 1;
    return 0;
}