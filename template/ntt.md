# description
ntt
# tabtrigger
ntt
# snippet
```cpp
namespace NTT {
    ll wl;
    vi w;
    ll qpow(ll x,ll y) {
        ll res = 1;
        while(y) {
            if(y&1) res = res*x%mod;
            x = x*x%mod;
            y >>= 1;
        }
        return res;
    }
    void get(ll n) {
        wl = 1;
        while(wl<n) wl<<=1;
    }
    void init(ll n) {
        ll t = 1;
        while((1<<t) < n) t++;
        t = min(t-1,21ll);
        w.resize((1<<t)+1);
        w[0] = 1;
        w[1<<t] = qpow(31,1<<21-t);
        for(ll i=t;i>=1;i--) w[1<<i-1] = w[1<<i]*w[1<<i] % mod;
        for(ll i=1;i<(1<<t);i++) w[i] = w[i&i-1]*w[i&-i] % mod;
    }
    void DIF(vi &a) {
        ll n = a.size();
        for(ll mid=n>>1;mid>=1;mid>>=1) {
            for(ll i=0,k=0;i<n;i+=mid<<1,k++) {
                forn(j,mid) {
                    ll x = a[i+j], y = a[i+j+mid]*w[k] % mod;
                    a[i+j] = (x+y) % mod;
                    a[i+j+mid] = (x-y+mod) % mod;
                }
            }
        }
    }
    void DIT(vi &a) {
        ll n = a.size();
        for(ll mid=1;mid<n;mid<<=1) {
            for(ll i=0,k=0;i<n;i+=mid<<1,k++) {
                forn(j,mid) {
                    ll x = a[i+j], y = a[i+j+mid];
                    a[i+j] = (x+y) % mod;
                    a[i+j+mid] = (x-y+mod)%mod*w[k]%mod;
                }
            }
        }
        ll inv = qpow(n,mod-2);
        forn(i,n) a[i] = a[i]*inv % mod;
        reverse(a.begin()+1,a.begin()+n);
    }
    vi mul(vi a,vi b) {
        ll n = a.size(), m = b.size();
        get(n+m);
        a.resize(wl);
        b.resize(wl);
        DIF(a), DIF(b);
        forn(i,wl) a[i] = a[i]*b[i] % mod;
        DIT(a);
        a.resize(n+m-1);
        return a;
    }
}
```