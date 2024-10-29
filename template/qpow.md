# description
qpow
# tabtrigger
qpow
# snippet
```cpp
ll qpow(ll x,ll y) {
    ll res = 1;
    while(y) {
        if(y&1) res = res*x%mod;
        x = x*x%mod;
        y >>= 1;
    }
    return res;
}
```