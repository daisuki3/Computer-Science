/*
gcd(a, b) = gcd(b, a % b)

证明：
g = gcd(a, b)

a = xg b = yg

a = kb + c
c = g(x - yk)
b,c的最大公因数为g

*/

int gcd(int a, int b){
    
    while( b != 0){
        int tmp = b;
        b = a % b;
        a = tmp;
    }

    return a;
}