#include <stdio.h>
#include <deque>
#include <bitset>
using namespace std;
#define mx 65536
#define us unsigned short
bitset<mx> seen;
deque<us> curr, best;
int main(){
    us x;
    int sz = 0;
    while (true){
        scanf("%d", &x);
        if (x == 0) break;
        curr.push_back(x);
        while (seen[x]){
            seen[curr.front()] = 0;
            best.push_back(curr.front());
            curr.pop_front();
        }
        while (best.size() > sz)
            best.pop_back();

        if (curr.size() > sz){
            best.clear();
            sz = curr.size();
        }
        seen[x] = 1;
    }
    //cout << "sz is: " << sz << "\n";
    for (int x: best){
        if (!sz) return 0;
        printf("%d\n", x);
        sz--;

    }
    for (int x: curr){
        if (!sz)return 0;
        printf("%d\n", x);
        sz--;
    }
    return 0;
}
/*
5 < [] 5
7 < [] 5 7
4 < [] 5 7 4
3 < [] 5 7 4 3
2 < [] 5 7 4 3 2
4 < [5 7 4] 3 2 4
5 < [5 7 4] 3 2 4 5
6 < [5 7 4] 3 2 4 5 6
7 < 3 2 4 5 6 7
8 < 3 2 4 5 6 7 8
6 < [3 2 4 5 6] 7 8 6
5 < [3 2 4 5 6] 7 8 6 5
3 < [3 2 4 5 6] 7 8 6 5 3
4 < [3 2 4 5 6] 7 8 6 5 3 4
5 < [3 2 4 5 6 7 8] 3 4
0*/