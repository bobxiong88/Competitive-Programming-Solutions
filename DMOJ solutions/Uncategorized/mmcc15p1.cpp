#include <bits/stdc++.h>
using namespace std;
int s[500001];
int parent[500001];
deque<pair<int,int>> d;
int findSet(int v){
    if (v == parent[v])
        return v;
    return findSet(parent[v]);
}
void Init(int N){
    for(int v = 1; v<=N;v++){
        s[v] = 1;
        parent[v] = v;
    }
}
void AddEdge(int U, int V){
    U = findSet(U);
    V = findSet(V);
    if (U != V) {
        if (s[U] < s[V])
            swap(U, V);
        parent[V] = U;
        s[U] += s[V];
        d.push_front(make_pair(U,V));
    }
    else
        d.push_front(make_pair(0,0));
}
void RemoveLastEdge(){
    int U = d.front().first;
    int V = d.front().second;
    d.pop_front();
    if(U!=0 && V!=0){
        parent[U] = U;
        parent[V] = V;
        s[U]-=s[V];
    }
}
int GetSize(int U){
    return s[findSet(U)];
}

int main(){
    /*
    Init(7);
    AddEdge(1,2);
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";
    AddEdge(3,4);
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";
    AddEdge(2,3);
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";
    AddEdge(2,5);
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";
    AddEdge(2,6);
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";

    RemoveLastEdge();
    cout << GetSize(2) << "\n";
    cout << "parent " << findSet(2) << "\n";
    */
}