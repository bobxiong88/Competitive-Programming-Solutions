import sys
input = sys.stdin.readline
def m(A, n, k): 
  
    # sorting given input array 
    A.sort() 
  
    # variable to store final product of  
    # all element of sub-sequence of size k 
    product = 1
  
    # CASE I 
    # If max element is 0 and 
    # k is odd then max product will be 0 
    if (A[n - 1] == 0 and (k & 1)): 
        return 0
  
    # CASE II 
    # If all elements are negative and 
    # k is odd then max product will be 
    # product of rightmost-subarray of size k 
    if (A[n - 1] <= 0 and (k & 1)) : 
        for i in range(n-1, n-k-1, -1): 
            product *= A[i] 
        return product 
  
    # else 
    # i is current left pointer index 
    i = 0
  
    # j is current right pointer index 
    j = n - 1
  
    # CASE III 
    # if k is odd and rightmost element in 
    # sorted array is positive then it 
    # must come in subsequence 
    # Multiplying A[j] with product and 
    # correspondingly changing j 
    if (k & 1): 
        product *= A[j] 
        j-= 1
        k-=1
  
    # CASE IV 
    # Now k is even. So, Now we deal with pairs 
    # Each time a pair is multiplied to product 
    # ie.. two elements are added to subsequence  
    # each time. Effectively k becomes half 
    # Hence, k >>= 1 means k /= 2 
    k >>= 1
  
    # Now finding k corresponding pairs to get 
    # maximum possible value of product 
    for itr in range( k) : 
  
        # product from left pointers 
        left_product = A[i] * A[i + 1] 
  
        # product from right pointers 
        right_product = A[j] * A[j - 1] 
  
        # Taking the max product from two  
        # choices. Correspondingly changing 
        # the pointer's position 
        if (left_product > right_product) : 
            product *= left_product 
            i += 2
          
        else : 
            product *= right_product 
            j -= 2
  
    # Finally return product 
    return product 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(m(a, n, 5))
