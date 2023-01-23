#include <iostream>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <cassert>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;

using namespace __gnu_pbds;

typedef
tree<
  int,
  null_type,
  greater_equal<int>,
  rb_tree_tag,
  // This policy updates nodes' metadata for order statistics.
  tree_order_statistics_node_update>
set_t;
int main()
{  
  int n;
  cin >> n;
  set_t s;
  long long t;
  t = 0;
  for(int i=0;i<n;i++){
    int score;
    cin >> score;
    s.insert(score);
    t+= s.order_of_key(score) +1;
  }
  printf("%.2f",double(t)/double(n));
  return 0;
}