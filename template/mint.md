# description
mint
# tabtrigger
mint
# snippet
```cpp
template<const ll T>
struct ModInt {
    const static ll mod = T;
    ll x;
    ModInt(ll x = 0) : x((x%mod+mod)%mod) {}
    ll val() { return x; }
    ModInt operator + (const ModInt &a) const { ll x0 = x + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    ModInt operator - (const ModInt &a) const { ll x0 = x - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    ModInt operator * (const ModInt &a) const { return ModInt(1LL * x * a.x % mod); }
    ModInt operator / (const ModInt &a) const { return *this * a.inv(); }
    bool operator == (const ModInt &a) const { return x == a.x; };
    bool operator != (const ModInt &a) const { return x != a.x; };
    void operator += (const ModInt &a) { x += a.x; if (x >= mod) x -= mod; }
    void operator -= (const ModInt &a) { x -= a.x; if (x < 0) x += mod; }
    void operator *= (const ModInt &a) { x = 1LL * x * a.x % mod; }
    void operator /= (const ModInt &a) { *this = *this / a; }
    friend ModInt operator + (ll y, const ModInt &a){ ll x0 = y + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    friend ModInt operator - (ll y, const ModInt &a){ ll x0 = y - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    friend ModInt operator * (ll y, const ModInt &a){ return ModInt(1LL * y * a.x % mod);}
    friend ModInt operator / (ll y, const ModInt &a){ return ModInt(y) / a;}
    friend ostream &operator<<(ostream &os, const ModInt &a) { return os << a.x;}
    friend istream &operator>>(istream &is, ModInt &t){return is >> t.x;}

    ModInt pow(int64_t n) const {
        ModInt res(1), mul(x);
        while(n){
            if (n & 1) res *= mul;
            mul *= mul;
            n >>= 1;
        }
        return res;
    }
    
    ModInt inv() const {
        ll a = x, b = mod, u = 1, v = 0;
        while (b) {
            ll t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        if (u < 0) u += mod;
        return u;
    }
};
using mint = ModInt<998244353>;
// using mint = ModInt<1000000007>;
// #define USE_C
#ifdef USE_C
    const int NC = 2e5+10;
    mint f[NC],vf[NC];

    auto init = []() {
        f[0] = vf[0] = 1;
        fore(i,1,NC-1) f[i] = f[i-1]*i;
        vf[NC-1] = f[NC-1].inv();
        for(int i=NC-2;i>=1;--i) vf[i] = vf[i+1]*(i+1);
        return 0;
    } ();

    mint C(int x,int y) {
        return f[x]*vf[y]*vf[x-y];
    }
#endif
```