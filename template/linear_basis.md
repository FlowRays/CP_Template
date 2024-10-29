# description
linear_basis
# tabtrigger
lb
# snippet
```cpp
template<const int M>
struct LinearBasis {
    array<int,M> a = {};
    array<int,M> t = {};
    int sz = 0;
 
    bool add(int x,int y = inf) {
        for(int i=M-1;i>=0;--i) {
            if(x>>i&1) {
                if(!a[i]) {
                    a[i] = x;
                    t[i] = y;
                    sz++;
                    return true;
                }
                if(y > t[i]) {
                    swap(a[i],x);
                    swap(t[i],y);
                }
                x ^= a[i];
            }
        }
        return false;
    }
 
    void operator+=(const LinearBasis &t) {
        forn(i,M) {
            if(t.a[i]) add(t.a[i],t.t[i]);
        }
    }
 
    LinearBasis operator+(const LinearBasis &a) const {
        auto res = *this;
        res += a;
        return res;
    }
 
    bool query(int x,int y = 0) {
        for(int i=M-1;i>=0;--i) {
            if((x>>i&1) && t[i] >= y) {
                x ^= a[i];
            }
        }
        return x == 0;
    }

    int qmax(int x = 0,int y = 0) {
        for(int i=M-1;i>=0;--i) {
            if(a[i] && t[i] >= y) x = max(x,x^a[i]);
        }
        return x;
    }
};
using lb = LinearBasis<30>;
```